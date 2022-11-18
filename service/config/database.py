from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values
import os
# settings = dotenv_values('./venv/.env')
# user = settings['RDS_USER']
# password =  settings['RDS_PASSWORD']
# rds_link = settings['RDS_LINK']
# port = settings['RDS_PORT']
# database = settings['RDS_DB_NAME']
database = str (os.environ["RDS_URL"])
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{rds_link}:{port}/{database}")
engine = create_engine(database)
meta = MetaData()
conn = engine.connect()