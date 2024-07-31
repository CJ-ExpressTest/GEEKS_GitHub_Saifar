import sqlalchemy as sa
from urllib.parse import quote
import pandas as pd
import numpy as np

origin_conn_str =  f"mssql+pymssql://sa:{quote('Ntip2P@ssw0rd')}@10.21.2.17:1433/TB"
origin_engine = sa.create_engine(origin_conn_str)
origin_conn = origin_engine.connect()


def change_sex(sex):
    if sex == "Male":
        return "ชาย"
    else:
        return "หญิง"


Contact_in_tb = pd.read_sql("select * from GEEKS1_CONTACT_IN_TB" ,origin_conn_str,dtype={"TB_ID":int, "PATIENT_ID":int, "HOUSE_CONTACT":str, "HOUSE_L_5":str, "HOUSE_518":str, "HOUSE_M_18":str,  "CLOSE_CONTACT":str })

tb_and_Index = pd.read_sql("select * from GEEKS2_TB_A_INDEX" ,origin_conn_str, dtype={"HCONTACT_ID":str, "REGIS_ID":str,"TB_ID":str, "TBNO":str, "MOL_ID":str, "TECHNIC":str, "RESULT":str, "AFB_ID":str, "AFB_RESULT":str, "RISK_TYPE":str,  "DESCRIPTION_TH":str })

status_tb_contact = pd.read_sql("select * from GEEKS3_STATUS_TB_CONTACT" ,origin_conn_str, dtype={"TB_ID":int})



Contact_in_tb["GENDER"]  = Contact_in_tb['GENDER'].map(change_sex)






DIALECT = "mysql"
SQL_DRIVER = "pymysql"
USERNAME = "USER"
PASSWORD = "USER"
HOST = "tbcontact-db"
PORT = 3306
DBNAME = "tbcontact"


conn_str = DIALECT + "+" + SQL_DRIVER + "://" + USERNAME + ":" +quote(PASSWORD) + "@" + HOST + ":" +str(PORT) + "/" + DBNAME


engine = sa.create_engine(conn_str)
conn = engine.connect()


Contact_in_tb.to_sql("Contact_in_tb", conn, index=False, if_exists="append")
tb_and_Index.to_sql("tb_and_Index", conn, index=False, if_exists="append")
status_tb_contact.to_sql("status_tb_contact" , conn , index=False, if_exists="append")



conn.close()
