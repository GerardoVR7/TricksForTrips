from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, JSON
from config.database import meta, engine

mexico_cities = Table(
    "mexico_cities",
    meta,
    Column("id", Integer, primary_key= True, autoincrement= True),
    Column("name", String(50)),
    Column("description", String(100)),
    Column("assessment", JSON),
    Column("photo_url", String(50))
)

meta.create_all(engine)