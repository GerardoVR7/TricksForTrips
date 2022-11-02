from sqlalchemy import Column, Float, Table, ForeignKey, Time
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

tours = Table(
    "tours",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_agency", Integer, ForeignKey("agencies.id")),
    Column("id_activity", Integer, ForeignKey("activities.id")),
    Column("place_name", String(100)),
    Column("description", String(255)),
    Column("capacity", Integer),
    Column("inclued_services", String(255)),
    Column("start_time", Time),
    Column("return_time", Time),
    Column("interest_points", String(255)),
    Column("price", Float),
    Column("min_number_people", String(255)),
    Column("location", String(255))
)

meta.create_all(engine)