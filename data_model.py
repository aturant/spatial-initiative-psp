from pydantic import BaseModel, conint, confloat, constr,ValidationError, validator, PositiveFloat
from datetime import datetime
from enum import Enum
from typing import Optional
from .utilities import *
logger = logging.getLogger(__name__)

class rodzaj_psp(str, Enum):
    p = 1
    z = 2
    f = 3

@pynocular.database_model.database_model("psp_raw", db_info)
class psp_line(BaseModel):
    meld_id:constr(regex = '[0-9/-//]+') #"0409001-3/2010"
    dl_geogr:Optional[PositiveFloat]
    sz_geogr:Optional[PositiveFloat]
    rodzaj:conint(ge=1, le=3)
    f_mz_rodz_1:Optional[bool]
    f_mz_rodz_2:Optional[bool]
    f_mz_rodz_3:Optional[bool]
    f_mz_rodz_4:Optional[bool]
    f_mz_rodz_5:Optional[bool]
    f_mz_rodz_6:Optional[bool]
    f_mz_rodz_7:Optional[bool]
    f_mz_rodz_8:Optional[bool]
    f_mz_rodz_9:Optional[bool]
    f_mz_rodz_10:Optional[bool]
    f_mz_rodz_11:Optional[bool]
    f_mz_rodz_12:Optional[bool]
    f_mz_rodz_13:Optional[bool]
    f_mz_rodz_14:Optional[bool]
    teryt:constr(regex = '[0-9]{6}')
    woj:str
    pow:str
    gmi:str
    miejscowosc:str
    obiekt_kod:conint(ge = 1)
    wlasciciel_kod:conint(ge = 1)
    data_zgl:Optional[datetime]
    data_doj:Optional[datetime]
    data_lok:Optional[datetime]
    data_usu:Optional[datetime]
    jrg_s:conint(ge = 0)
    jrg_ludz:conint(ge = 0)
    ospk_s:conint(ge = 0)
    ospk_ludz:conint(ge = 0)
    osp_s:conint(ge = 0)
    osp_ludz:conint(ge = 0)
    f_rodz_dz_lo_1:Optional[bool]
    f_rodz_dz_lo_2:Optional[bool]
    f_rodz_dz_lo_3:Optional[bool]
    f_rodz_dz_lo_4:Optional[bool]
    f_rodz_dz_lo_5:Optional[bool]
    f_rodz_dz_lo_6:Optional[bool]
    f_rodz_dz_lo_7:Optional[bool]
    f_rodz_dz_lo_8:Optional[bool]
    f_rodz_dz_lo_9:Optional[bool]
    f_rodz_dz_lo_10:Optional[bool]
    f_rodz_dz_lo_11:Optional[bool]
    f_rodz_dz_lo_12:Optional[bool]
    f_rodz_dz_lo_13:Optional[bool]
    f_rodz_dz_lo_14:Optional[bool]
    f_rodz_dz_lo_15:Optional[bool]
    f_rodz_dz_lo_16:Optional[bool]
    f_rodz_dz_lo_17:Optional[bool]
    f_rodz_dz_lo_18:Optional[bool]
    f_rodz_dz_lo_19:Optional[bool]
    f_rodz_dz_lo_20:Optional[bool]
    f_rodz_dz_lo_21:Optional[bool]
    f_rodz_dz_lo_22:Optional[bool]
    f_rodz_dz_lo_23:Optional[bool]
    f_rodz_dz_lo_24:Optional[bool]
    f_rodz_dz_lo_25:Optional[bool]
    f_rodz_dz_lo_26:Optional[bool]
    f_rodz_dz_lo_27:Optional[bool]
    f_rodz_dz_lo_28:Optional[bool]
    f_rodz_dz_lo_29:Optional[bool]
    f_rodz_dz_lo_30:Optional[bool]
    f_rodz_dz_lo_31:Optional[bool]
    f_rodz_dz_lo_32:Optional[bool]
    f_rodz_dz_hi_1:Optional[bool]
    f_rodz_dz_hi_2:Optional[bool]
    f_rodz_dz_hi_3:Optional[bool]
    f_rodz_dz_hi_4:Optional[bool]
    f_rodz_dz_hi_5:Optional[bool]
    f_rodz_dz_hi_6:Optional[bool]
    f_rodz_dz_hi_7:Optional[bool]
    f_rodz_dz_hi_8:Optional[bool]
    f_rodz_dz_hi_9:Optional[bool]
    f_rodz_dz_hi_10:Optional[bool]
    f_rodz_dz_hi_11:Optional[bool]
    f_rodz_dz_hi_12:Optional[bool]
    f_uzyt_sp_1:Optional[bool]
    f_uzyt_sp_2:Optional[bool]
    f_uzyt_sp_3:Optional[bool]
    f_uzyt_sp_4:Optional[bool]
    f_uzyt_sp_5:Optional[bool]
    f_uzyt_sp_6:Optional[bool]
    f_uzyt_sp_7:Optional[bool]
    f_uzyt_sp_8:Optional[bool]
    f_uzyt_sp_9:Optional[bool]
    f_uzyt_sp_10:Optional[bool]
    f_uzyt_sp_11:Optional[bool]
    f_uzyt_sp_12:Optional[bool]
    f_uzyt_sp_13:Optional[bool]
    f_uzyt_sp_14:Optional[bool]
    f_uzyt_sp_15:Optional[bool]
    f_uzyt_sp_16:Optional[bool]
    f_uzyt_sp_17:Optional[bool]
    f_uzyt_sp_18:Optional[bool]
    f_uzyt_sp_19:Optional[bool]
    f_uzyt_sp_20:Optional[bool]
    f_uzyt_sp_21:Optional[bool]
    f_uzyt_sp_22:Optional[bool]
    f_uzyt_sp_23:Optional[bool]
    f_uzyt_sp_24:Optional[bool]
    f_uzyt_sp_25:Optional[bool]
    f_uzyt_sp_26:Optional[bool]
    f_uzyt_sp_27:Optional[bool]
    f_uzyt_sp_28:Optional[bool]
    f_uzyt_sp_29:Optional[bool]
    f_uzyt_sp_30:Optional[bool]
    f_uzyt_sp_31:Optional[bool]
    f_uzyt_sp_32:Optional[bool]
    f_miej_dz_1:Optional[bool]
    f_miej_dz_2:Optional[bool]
    f_miej_dz_3:Optional[bool]
    f_miej_dz_4:Optional[bool]
    f_miej_dz_5:Optional[bool]
    f_miej_dz_6:Optional[bool]
    f_miej_dz_7:Optional[bool]
    f_miej_dz_8:Optional[bool]
    f_miej_dz_9:Optional[bool]
    f_miej_dz_10:Optional[bool]
    f_miej_dz_11:Optional[bool]
    wlk_pow:float
    wlk_kub:float
    straty:confloat(ge = 0)
    straty_bud:confloat(ge = 0)
    uratowano:confloat(ge = 0)
    przyczyna_kod:int
    przyczyna_opis:str
    f_inst_1:Optional[bool]
    f_inst_2:Optional[bool]
    f_inst_3:Optional[bool]
    f_inst_4:Optional[bool]
    f_inst_5:Optional[bool]
    f_inst_6:Optional[bool]
    f_inst_7:Optional[bool]
    f_inst_8:Optional[bool]
    f_inst_9:Optional[bool]
    f_inst_10:Optional[bool]
    f_inst_11:Optional[bool]
    f_inst_12:Optional[bool]
    f_inst_13:Optional[bool]
    f_inst_14:Optional[bool]
    f_inst_15:Optional[bool]
    f_opis_ob_1:Optional[bool]
    f_opis_ob_2:Optional[bool]
    f_opis_ob_3:Optional[bool]
    f_opis_ob_4:Optional[bool]
    f_opis_ob_5:Optional[bool]
    f_opis_ob_6:Optional[bool]
    f_opis_ob_7:Optional[bool]
    onz:Optional[str]
    f_wybuch_1:Optional[bool]
    f_wybuch_2:Optional[bool]
    f_wybuch_3:Optional[bool]
    wlk_ob_dl:Optional[conint(ge=0) ]
    wlk_ob_sz:Optional[conint(ge=0) ]
    wlk_ob_wy:Optional[conint(ge=0) ]
    f_dost_2:Optional[bool]
    f_dost_4:Optional[bool]
    f_dost_6:Optional[bool]
    
    @validator('onz', pre = True)
    def clean_txt(cls, val):
        if val:
            val = val.upper().strip()
        return val if len(val) else None
    
    @validator('data_zgl', 'data_doj', 'data_lok', 'data_usu', pre=True)
    def parse_date(cls, val):
        val = cls.clean_txt(val)
        try:
            if val:
                val = val.split(",")[0]
                #10/01/19 07:58:00,000000000
            ret_val = datetime.strptime(val, '%y/%m/%d %H:%M:%S') if val else val
        except:
            logger.error(f' {val} not converted to date')
        finally:
            return ret_val

    @validator('dl_geogr','sz_geogr', 
               'wlk_ob_dl', 'wlk_ob_sz', 'wlk_ob_wy', pre = True)
    def zeroify(cls, val):
        val = cls.str2dp(val)
        return None if val is None or round(float(val),2) == 0.00 else val
    
    # @validator('ONZ', pre = True)
    # def Listify(cls, val):
    #     ret_val = []
    #     for el in val.split(','):
    #         _ = cls.str2dp(el)
    #         if _:
    #             ret_val.append(_)
    #     return ret_val if len(ret_val) else None
    
    @validator(
               'straty', 'straty_bud', 'uratowano',
                'wlk_kub', 'wlk_pow',
               pre = True)
    def str2dp(cls, val):
        val = val.upper().strip()
        ret_val = None
        if val == '':
            return None
        try:
            ret_val = locale.atof(val)
            # ret_val = ret_val if ret_val>0 else None
        except ValueError:
            logger.error(f'{val} not converted to float')
        finally:
            return ret_val
        
    @validator('f_mz_rodz_1',
               'f_mz_rodz_2',
               'f_mz_rodz_3',
               'f_mz_rodz_4',
               'f_mz_rodz_5',
               'f_mz_rodz_6',
               'f_mz_rodz_7',
               'f_mz_rodz_8',
               'f_mz_rodz_9',
               'f_mz_rodz_10',
               'f_mz_rodz_11',
               'f_mz_rodz_12',
               'f_mz_rodz_13',
               'f_mz_rodz_14',
               'f_rodz_dz_lo_1',
               'f_rodz_dz_lo_2',
               'f_rodz_dz_lo_3',
               'f_rodz_dz_lo_4',
               'f_rodz_dz_lo_5',
               'f_rodz_dz_lo_6',
               'f_rodz_dz_lo_7',
               'f_rodz_dz_lo_8',
               'f_rodz_dz_lo_9',
               'f_rodz_dz_lo_10',
               'f_rodz_dz_lo_11',
               'f_rodz_dz_lo_12',
               'f_rodz_dz_lo_13',
               'f_rodz_dz_lo_14',
               'f_rodz_dz_lo_15',
               'f_rodz_dz_lo_16',
               'f_rodz_dz_lo_17',
               'f_rodz_dz_lo_18',
               'f_rodz_dz_lo_19',
               'f_rodz_dz_lo_20',
               'f_rodz_dz_lo_21',
               'f_rodz_dz_lo_22',
               'f_rodz_dz_lo_23',
               'f_rodz_dz_lo_24',
               'f_rodz_dz_lo_25',
               'f_rodz_dz_lo_26',
               'f_rodz_dz_lo_27',
               'f_rodz_dz_lo_28',
               'f_rodz_dz_lo_29',
               'f_rodz_dz_lo_30',
               'f_rodz_dz_lo_31',
               'f_rodz_dz_lo_32',
               'f_rodz_dz_hi_1',
               'f_rodz_dz_hi_2',
               'f_rodz_dz_hi_3',
               'f_rodz_dz_hi_4',
               'f_rodz_dz_hi_5',
               'f_rodz_dz_hi_6',
               'f_rodz_dz_hi_7',
               'f_rodz_dz_hi_8',
               'f_rodz_dz_hi_9',
               'f_rodz_dz_hi_10',
               'f_rodz_dz_hi_11',
               'f_rodz_dz_hi_12',
               'f_uzyt_sp_1',
               'f_uzyt_sp_2',
               'f_uzyt_sp_3',
               'f_uzyt_sp_4',
               'f_uzyt_sp_5',
               'f_uzyt_sp_6',
               'f_uzyt_sp_7',
               'f_uzyt_sp_8',
               'f_uzyt_sp_9',
               'f_uzyt_sp_10',
               'f_uzyt_sp_11',
               'f_uzyt_sp_12',
               'f_uzyt_sp_13',
               'f_uzyt_sp_14',
               'f_uzyt_sp_15',
               'f_uzyt_sp_16',
               'f_uzyt_sp_17',
               'f_uzyt_sp_18',
               'f_uzyt_sp_19',
               'f_uzyt_sp_20',
               'f_uzyt_sp_21',
               'f_uzyt_sp_22',
               'f_uzyt_sp_23',
               'f_uzyt_sp_24',
               'f_uzyt_sp_25',
               'f_uzyt_sp_26',
               'f_uzyt_sp_27',
               'f_uzyt_sp_28',
               'f_uzyt_sp_29',
               'f_uzyt_sp_30',
               'f_uzyt_sp_31',
               'f_uzyt_sp_32',
               'f_miej_dz_1',
               'f_miej_dz_2',
               'f_miej_dz_3',
               'f_miej_dz_4',
               'f_miej_dz_5',
               'f_miej_dz_6',
               'f_miej_dz_7',
               'f_miej_dz_8',
               'f_miej_dz_9',
               'f_miej_dz_10',
               'f_miej_dz_11',
               'f_inst_1',
               'f_inst_2',
               'f_inst_3',
               'f_inst_4',
               'f_inst_5',
               'f_inst_6',
               'f_inst_7',
               'f_inst_8',
               'f_inst_9',
               'f_inst_10',
               'f_inst_11',
               'f_inst_12',
               'f_inst_13',
               'f_inst_14',
               'f_inst_15',
               'f_opis_ob_1',
               'f_opis_ob_2',
               'f_opis_ob_3',
               'f_opis_ob_4',
               'f_opis_ob_5',
               'f_opis_ob_6',
               'f_opis_ob_7',
               'f_wybuch_1',
               'f_wybuch_2',
               'f_wybuch_3',
               'f_dost_2',
               'f_dost_4',
               'f_dost_6', pre=True)
    def TN_convert(cls, val:str):
        val = val.upper().strip()
        if val in ['T','Y']:
            ret_val = True
        elif val == 'N':
            ret_val = False
        elif val == '':
            ret_val = None
        else:
            logger.warning(f'Value {val} not in expected range')
        return ret_val
        
    class Config:
        alias_generator = str.upper
        anystr_strip_whitespace = True
        extra = 'forbid'
        


if __name__ == '__main__':
    if True:
        from pynocular.db_util import create_table
        asyncio.run( create_table(db_info, psp_line._table))
        print('fin')