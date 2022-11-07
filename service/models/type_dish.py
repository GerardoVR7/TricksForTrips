from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

type_dish = Table(
    "type_dish",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("type",String(255),)
)

meta.create_all(engine)