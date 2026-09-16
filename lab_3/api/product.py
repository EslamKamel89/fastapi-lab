from typing import Annotated

from core.db import get_async_session
from crud import create_product, get_all_products, get_product_by_id
from fastapi import APIRouter, Depends, HTTPException, status
from schemas import ProductCreate, ProductPublic
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter(prefix="/products", tags=["products"])

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


@router.post("/", response_model=ProductPublic, status_code=status.HTTP_201_CREATED)
async def create_new_product(session: SessionDep, product_data: ProductCreate):
    return await create_product(product_data, session)


@router.get("/", response_model=list[ProductPublic])
async def get_products(session: SessionDep):
    return await get_all_products(session)


@router.get("/{product_id}", response_model=ProductPublic)
async def get_product(product_id: int, session: SessionDep):
    product = await get_product_by_id(product_id, session)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
    return product
