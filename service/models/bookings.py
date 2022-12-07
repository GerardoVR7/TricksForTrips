from sqlalchemy import Column, Float, Table, ForeignKey, Date
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

booking = Table(
    "booking",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_tourist", Integer),
    Column("id_tour", Integer),
    Column("id_agency", Integer),
    Column("tourist_name", String(50)),
    Column("date", Date),
    Column("adults", Integer),
    Column("childrens", Integer),
    Column("babys", Integer),
    Column("pets", Integer),
    Column("total", Float),
    Column("place_name", String(255))
)

meta.create_all(engine)