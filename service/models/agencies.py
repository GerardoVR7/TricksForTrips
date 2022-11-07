from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

agencies = Table(
    "agencies",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_city", Integer, ForeignKey("mexico_cities.id")),
    Column("name", String(255)),
    Column("address", String(255)),
    Column("RFC", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("url", String(255)),
    Column("agency_code", String(255)),
    Column("phone", String(15)),
    Column("postal_code", Integer)
)

meta.create_all(engine)