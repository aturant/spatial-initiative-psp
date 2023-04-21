from .data_model import *
from collections import defaultdict
from .utilities import *

logger = logging.getLogger(__name__)

path = '/home/alek/Documents/praca/SpatialInitiative/Dane/PSP/corr/dane.csv'

# path = '../Dane/PSP/sample.csv'
# {161: 1, 167: 4})


async def parser(
        id,
        config: dict):
    logger.info(f'Parser no:{id} up!')

    def self_status_write():   
        running_time = (datetime.now() - start_time).total_seconds()
        speed = (config["parser_statuser"][id]/running_time)
        logger.info(
            f'{id=} {config["parser_statuser"][id]=}. Speed is: {speed:.3f} it/sec.')

    while "task_txt_file_reader" not in config:
        await asyncio.sleep(1)
    logger.info(f'Parser no:{id} going!')
    start_time = datetime.now()
    try:
        while True:
            speed = 0
            
            line_number, line_item = await config["items_to_parse"].get()

            _ = psp_line.parse_obj(line_item)
            config["parsed_items"].append(_)
            config["parser_statuser"][id] += 1
            config["items_to_parse"].task_done()
            if config["parser_statuser"][id] % config["batch_size_db"] == 0:
                self_status_write()
            
    except asyncio.CancelledError as ce:
        logger.warning(
        f'Parser no:{id} is going down. It made {config["parser_statuser"][id]}.')
        self_status_write()

    except Exception as ex:
        
        logger.error(
            f'Some error,{line_number=} {line_item} {ex=}')
        config["parse_errors"].append(
            (line_number, ex, line_item)
        )


async def db_writer(
        config: dict):
    logger.info(f'DB writer up!')

    async def write_buffer():
        buffer = list()
        while len(config["parsed_items"]):
            buffer.extend(config["parsed_items"])
            config["parsed_items"].clear()

        logger.info(
                    f'Before db write. Buffer size: {len(buffer)}')


        if len(buffer):
                # await psp_line.create_list(buffer)
                # pynocular way
            headers = [*buffer[-1].dict().keys()]
            async with config["db_connection_pool"].connection() as aconn:
                async with aconn.cursor() as curr:
                    async with curr.copy(f"COPY data_staging.psp_raw ({','.join(headers)}) FROM STDIN") as copy:
                        for record in buffer:
                            record_ = [record.__dict__[x] for x in headers]
                            await copy.write_row(record_)

            await aconn.commit()
            return len(buffer)
        else:
            return 0


    def status_writer():
        logger.info(
            f'Wrote to db. {config["rows_written"]  = }. In here: {records_written}, {config["rows_read"]  = }')
        total = sum(config["parser_statuser"].values())
        any_status = [(k, round(v/total, 2))
            for k, v in config["parser_statuser"].items()]
        any_status = sorted(any_status, key=lambda x: x[0])
        logger.info(f'Current log is: {any_status}')

    start_time = datetime.now()
    try:  
        while True:
          
            if len(config["parsed_items"]) >= config["batch_size_db"]:

                records_written = await write_buffer()

                config["rows_written"] += records_written
                status_writer


            else:
                await asyncio.sleep(1)
    except asyncio.CancelledError:

        if len(config["parsed_items"]):
            raise Exception # to powinno byc puste
        logger.info('DB writer going down')
        config["rows_written"] += records_written
        status_writer



async def txt_file_reader(
        path: str,
        config: dict):
    logger.info(f'file reader  up!')

    async with aiofiles.open(path, mode='r', encoding='windows-1250') as f:
        dict_reader = aiocsv.AsyncDictReader(f, delimiter=';', quotechar="\"")
        logger.info(f'Opened: {path}')

        async for line_item in dict_reader:

            if config["items_to_parse"].full():
                await config["items_to_parse"].join()
                # wait for all the items to be eaten

            config['rows_read'] += 1
            await config["items_to_parse"].put(
                (config['rows_read'],
                 line_item))

            if config['rows_read'] % config["batch_size_db"] == 0:
                logger.info(f'{config["rows_read"]=}')
                logger.info(f'{config["rows_written"]=}')


    logger.info(
        f'file reader finished! Queue state is {config["items_to_parse"].qsize()}')
   
    await config["items_to_parse"].join()
    logger.info(
        f'file reader waited for queue to finish. Call to cancel parser tasks.')


    config["batch_size_db"] = 1
    await asyncio.sleep(3)
    logger.info(f'{config["rows_read"]=}')
    logger.info(f'{config["rows_written"]=}')
    #################################################################
    config["task_parsers"].cancel()
    logger.info(f'Parser tasks cancelled')
    config["task_db_writer"].cancel()
    logger.info(f'DB writer tasks cancelled')
    



async def main():
    config = {}
    config["parser_statuser"] = defaultdict(lambda: 0)

    config["items_to_parse"] = asyncio.Queue(30000)
    config["rows_read"] = 0
    config["db_connection_pool"] = AsyncConnectionPool(conninfo)

    config["parsed_items"] = []
    config["no_workers"] = 8
    config["batch_size_db"] = 100000
    config["rows_written"] = 0
    config["parse_errors"] = []

    config["task_txt_file_reader"] = asyncio.create_task(
        txt_file_reader(path, config), name='task_txt_file_reader')

    async with config["db_connection_pool"].connection() as aconn:
        async with aconn.cursor() as curr:
            await curr.execute(f'truncate data_staging.psp_raw;')

    parsers = [parser(
        id=i + 1,
        config=config)
        for i in range(config["no_workers"])]

    # same as create task, returns future object
    config["task_parsers"] = asyncio.gather(*parsers)
    config["task_db_writer"] = asyncio.create_task(db_writer(config), name='db_write')

    await asyncio.gather(config["task_txt_file_reader"],
                         config["task_parsers"],
                         config["task_db_writer"])
    logger.info(f'Done! {config=}')
    # db_info.close()
    logger.info(f'Read: { config["rows_read"]} lines')


if __name__ == '__main__':

    ######################################################

    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
    logger('All done!')
    loop.close()
