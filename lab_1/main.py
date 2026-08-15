from typing import Annotated

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "ok"}


class Item(BaseModel):
    id: int
    name: str
    price: float
    tax: float | None = None


items = [
    Item(
        id=i,
        name=f"Product-{i}",
        price=i * 100,
        tax=i / 10,
    )
    for i in range(1, 20)
]


@app.get("/items/get/{item_id}", response_model=Item)
async def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/items/all", response_model=list[Item])
async def get_items(
    skip: Annotated[int, Query(ge=0)], limit: Annotated[int, Query(ge=1)]
):
    return items[skip : skip + limit]


@app.get("/items/{item_name}")
async def get_item(
    item_name: Annotated[str, Path(min_length=3, max_length=100)],
    company: Annotated[str, Query()],
    count: Annotated[int, Query(ge=1)] = 1,
    rating: Annotated[int | None, Query(ge=1, le=5)] = None,
):
    return {
        "item": item_name,
        "company": company,
        "count": count,
        "rating": rating if rating else "You didn't leave a rating",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
