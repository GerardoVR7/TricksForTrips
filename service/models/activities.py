from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

activities = Table(
    "activities",
    meta,
    Column("id", Integer, primary_key= True, autoincrement=True),
    Column("name", String(255)),
    Column("time", String(255)),
    Column("price", Float)
)

meta.create_all(engine)