from sqlalchemy import Column, Float, Table, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

paypal = Table(
    "paypal",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_user", String(255)),
    Column("id_paypal", Integer),
    Column("date", DateTime),
    Column("total", Float)
)

meta.create_all(engine)