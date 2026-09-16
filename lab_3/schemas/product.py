from sqlmodel import SQLModel


class ProductBase(SQLModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    category_id: int


class ProductPublic(ProductBase):
    id: int
    category_id: int
