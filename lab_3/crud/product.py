from typing import Sequence

from models import Product
from schemas import ProductCreate
from sqlalchemy.orm import selectinload
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_product(product_data: ProductCreate, session: AsyncSession) -> Product:
    product = Product.model_validate(product_data)
    session.add(product)
    await session.commit()
    query = (
        select(Product)
        .where(Product.id == product.id)
        .options(selectinload(Product.category), selectinload(Product.reviews))  # type: ignore
    )
    return (await session.exec(query)).one()


async def get_all_products(session: AsyncSession) -> Sequence[Product]:
    query = select(Product).options(selectinload(Product.category), selectinload(Product.reviews))  # type: ignore
    result = await session.exec(query)
    return result.all()


async def get_product_by_id(product_id: int, session: AsyncSession) -> Product | None:
    query = (
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.category), selectinload(Product.reviews))  # type: ignore
    )
    result = await session.exec(query)
    return result.first()
