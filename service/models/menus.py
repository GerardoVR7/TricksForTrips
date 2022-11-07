from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

menus = Table(
    "menus",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_restaurant", Integer, ForeignKey("restaurants.id")),
    Column("name",String(255),)
)

meta.create_all(engine)