from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from lab_3.models.user import User


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    products: list["Product"] = Relationship(back_populates="category")


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str | None = None
    price: float
    category_id: int = Field(foreign_key="category.id")
    category: "Category" = Relationship(back_populates="products")
    reviews: list["Review"] = Relationship(back_populates="product")


class Review(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    rating: int
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")
    user: "User" = Relationship(back_populates="reviews")
    product: "Product" = Relationship(back_populates="reviews")
