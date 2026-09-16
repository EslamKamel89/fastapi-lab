from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from lab_3.models.product import Review


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    role: str = "customer"
    reviews: list["Review"] = Relationship(back_populates="user")
