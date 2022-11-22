from sqlalchemy import Column, Float, Table, ForeignKey, Time, JSON, Date
from sqlalchemy.sql.sqltypes import Integer, String
from ..config.database import meta, engine

tours = Table(
    "tours",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_agency", Integer, ForeignKey("agencies.id")),
    Column("id_activity", Integer, ForeignKey("activities.id")),
    Column("id_city", Integer, ForeignKey("mexico_cities.id")),
    Column("agency_name", String(50)),
    Column("place_name", String(100)),
    Column("description", String(255)),
    Column("capacity", Integer),
    Column("inclued_services", JSON),
    Column("start_time", Time),
    Column("return_time", Time),
    Column("interest_points", String(255)),
    Column("price", Float),
    Column("min_number_people", String(255)),
    Column("validity_start", Date),
    Column("validity_end", Date),
    Column("photo_name", String(100)),
    Column("photo_url", String(255)),
)

meta.create_all(engine)