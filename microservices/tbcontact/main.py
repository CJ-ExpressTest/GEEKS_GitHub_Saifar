from fastapi import FastAPI
import pandas as pd 
import sqlalchemy as sa
import requests

app = FastAPI()


@app.get("/")
async def root():

	conn_str = 'mysql+pymysql://user:user@tbcontact-db:3306/tbcontact'
	engine = sa.create_engine(conn_str)
	conn = engine.connect()
	tbcontact = pd.read_sql("Contact_in_tb", conn)
	conn.close()
	return tbcontact.to_dict("records")

 
 
	
@app.get("/status/")
async def status():
	return {'status': 'Online3'}









