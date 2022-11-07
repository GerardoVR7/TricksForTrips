from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:G7v3R2001@tricks4trips.ckn3utwh3nqz.us-east-1.rds.amazonaws.com:3306/tricksfortrips")
#engine = create_engine("mysql+pymysql://gerardo:password@50.19.131.119:3306/pruebas")
#engine = create_engine("mysql+pymysql://gerardo:G7v3R2001@localhost:3306/tricksfortrips")
meta = MetaData()

conn = engine.connect()