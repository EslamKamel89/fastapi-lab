from sqlmodel import SQLModel


class CategoryPublic(SQLModel):
    id: int
    name: str


class ReviewPublic(SQLModel):
    id: int
    text: str
    rating: int
    user_id: int
    product_id: int


class ProductBase(SQLModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    category_id: int


class ProductPublic(ProductBase):
    id: int
    category_id: int
    category: CategoryPublic
    reviews: list[ReviewPublic] = []
