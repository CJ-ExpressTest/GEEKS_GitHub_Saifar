from fastapi import FastAPI
import pandas as pd 
import sqlalchemy as sa
import requests

app = FastAPI()

@app.get("/")
async def root():
	return {'status': 'Online3'}



def get_Contact_in_tb_data():

	conn_str = 'mysql+pymysql://user:user@tbcontact-db:3306/tbcontact'
	engine = sa.create_engine(conn_str)
	conn = engine.connect()
	tbcontact = pd.read_sql("Contact_in_tb", conn)
	conn.close()
	
	return tbcontact


def get_status_tb_contact_data():

	conn_str = 'mysql+pymysql://user:user@tbcontact-db:3306/tbcontact'
	engine = sa.create_engine(conn_str)
	conn = engine.connect()
	statustbcontact = pd.read_sql("status_tb_contact", conn)
	conn.close()
	
	return statustbcontact


def get_tb_and_Index_data():

	conn_str = 'mysql+pymysql://user:user@tbcontact-db:3306/tbcontact'
	engine = sa.create_engine(conn_str)
	conn = engine.connect()
	tbindex = pd.read_sql("tb_and_Index", conn)
	conn.close()
	
	return tbindex

 
 

@app.get("/tbcontact/")
async def tbcontact():
	tbcontact = get_Contact_in_tb_data()
	return tbcontact.to_dict("records")

@app.get("/statustbcontact/")
async def statustbcontact():
	statustbcontact = get_status_tb_contact_data()
	return statustbcontact.to_dict("records")


@app.get("/tbindex/")
async def tbindex():
	tbindex = get_tb_and_Index_data()
	return tbindex.to_dict("records")


