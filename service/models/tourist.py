from sqlalchemy import Column, DateTime, Float, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

tourist = Table(
    "tourist",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("lastname", String(50)),
    Column("email", String(100)),
    Column("password", String(255)),
    Column("phone", String(15)),
    Column("address", String(50)),
    Column("postal_code", Integer),
    Column("country", String(50))
)

meta.create_all(engine)