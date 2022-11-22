from sqlalchemy import create_engine, MetaData
import os

database = str (os.environ["RDS_URL"])
engine = create_engine(database)
meta = MetaData()
conn = engine.connect()