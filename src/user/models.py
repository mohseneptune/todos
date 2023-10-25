from sqlalchemy import Column, DateTime, Integer, String, Table

from core.postgres import mapper_registry
from user.entities import User

user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("mobile", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("first_name", String, nullable=True),
    Column("last_name", String, nullable=True),
    Column("email", String, nullable=True),
    Column("registration_date", DateTime, nullable=False),
)


def start_mapper() -> None:
    mapper_registry.map_imperatively(User, user_table)
