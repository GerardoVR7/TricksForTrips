from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

tours_services = Table(
    "tours_services",
    meta,
    Column("id", Integer, primary_key= True, autoincrement= True),
    Column("name", String(50))
)

meta.create_all(engine)