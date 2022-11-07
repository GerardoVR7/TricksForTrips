from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

mexico_cities = Table(
    "mexico_cities",
    meta,
    Column("id", Integer, primary_key= True, autoincrement= True),
    Column("name", String(50))
)

meta.create_all(engine)