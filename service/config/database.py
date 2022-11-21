from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values
import os

database = str (os.environ["RDS_URL"])
engine = create_engine(database)
meta = MetaData()
conn = engine.connect()