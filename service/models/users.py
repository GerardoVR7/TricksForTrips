from sqlalchemy import Column, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key= True, autoincrement= True),
    Column("email", String(50)),
    Column("password", String(50))
)

meta.create_all(engine)