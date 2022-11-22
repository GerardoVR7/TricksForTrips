from sqlalchemy import create_engine, MetaData
import os

database = str ("mysql+pymysql://admin:G7v3R2001@pruebas.ckn3utwh3nqz.us-east-1.rds.amazonaws.com:3306/tricksfortrips")
engine = create_engine(database)
meta = MetaData()
conn = engine.connect()