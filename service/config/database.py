from sqlalchemy import create_engine, MetaData
from dotenv import dotenv_values

settings = dotenv_values('./venv/.env')
user = settings['RDS_USER']
password =  settings['RDS_PASSWORD']
rds_link = settings['RDS_LINK']
port = settings['RDS_PORT']
database = settings['RDS_DB_NAME']

engine = create_engine(f"mysql+pymysql://{user}:{password}@{rds_link}:{port}/{database}")
meta = MetaData()
conn = engine.connect()