import locale
import pynocular #alchemy wrapper. tworzy tabele z modeli pydantic
from psycopg_pool import ConnectionPool, AsyncConnectionPool

from typing import List
locale.setlocale(locale.LC_ALL,"pl_PL.UTF-8")
import csv
import logging
import asyncio, aiofiles, aiocsv
from collections import defaultdict
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
    filename='./main_psp.log',
    filemode='w',
    encoding='utf-8', 
    level=logging.INFO)

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)



logging.info("Hello world!")

conninfo = {
    "dbname":"spatial",
    "user":"data_staging_inserter",
    "password":"data_staging_inserter",
    "port":5435,
    "host":"127.0.0.1"}

connection_string  = f"postgresql://{conninfo['user']}:{conninfo['password']}@localhost:{conninfo['port']}/{conninfo['dbname']}?sslmode=disable"

db_info = pynocular.engines.DBInfo(connection_string)


conninfo = \
    "dbname=spatial \
    user=data_staging_inserter \
    password=data_staging_inserter \
    port=5435 \
    host = 127.0.0.1"

# def pool_create():
#     # pool = AsyncConnectionPool(conninfo)
#     pool = ConnectionPool(conninfo)
#     return pool