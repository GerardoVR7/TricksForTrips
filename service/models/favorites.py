from sqlalchemy import Column, Float, Table, ForeignKey, Time, JSON, Date
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

favorites = Table(
    "favorites",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_tour", Integer),
    Column("id_user", Integer)
)

meta.create_all(engine)