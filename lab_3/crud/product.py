from typing import Sequence

from models import Product
from schemas import ProductCreate
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def create_product(product_data: ProductCreate, session: AsyncSession) -> Product:
    product = Product.model_validate(product_data)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def get_all_products(session: AsyncSession) -> Sequence[Product]:
    query = select(Product)
    result = await session.exec(query)
    return result.all()


async def get_product_by_id(product_id: int, session: AsyncSession) -> Product | None:
    query = select(Product).where(Product.id == product_id)
    result = await session.exec(query)
    return result.first()
