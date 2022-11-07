from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

dishes = Table(
    "dishes",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_menu", Integer, ForeignKey("menus.id")),
    Column("id_type", Integer, ForeignKey("type_dish.id")),
    Column("description", String(255)),
    Column("name",String(255),),
    Column("principal_ingredient", String(255)),
    Column("price", Float)
)

meta.create_all(engine)