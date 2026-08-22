import json
from typing import Annotated

import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, StringConstraints, validate_call
from pydantic_core._pydantic_core import ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., min_length=4)
    description: str | None = None
    price: float


class Offer(BaseModel):
    offer: float | None = None


@app.post("/item")
async def create_item(
    item: Item = Body(...),
    offer: Offer = Body(...),
    flower: str = Body(...),
):
    return {"item": item, "offer": offer}


# @app.post("/item")
# async def create_item(
#     name: str = Body(...),
#     description: str | None = Body(None),
#     price: float = Body(),
#     offer: float | None = Body(None),
# ):
#     items = {
#         "name": name,
#         "description": description,
#         "price": price,
#         "offer": offer,
#     }
#     return {k: v for (k, v) in items.items() if v is not None}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
