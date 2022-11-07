from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

restaurants = Table(
    "restaurants",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("address", String(255)),
    Column("RFC", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("url", String(255)),
    Column("cellphone", String(15)),
    Column("postal_code", Integer)
)

meta.create_all(engine)