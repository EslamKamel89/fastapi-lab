import json
from typing import Annotated

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field, StringConstraints, validate_call
from pydantic_core._pydantic_core import ValidationError

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., min_length=3)
    description: str | None = None
    price: float


@validate_call
def validate_name(name: Annotated[str, StringConstraints(min_length=4)]):
    return name


@app.get("/test")
async def test():
    try:
        name = validate_name("Ali")
        print("name is valid")
        return name
    except ValidationError as e:
        print("Name not valid")
        print(e)
        return json.loads(e.json())


@app.post("/item", response_model=Item)
async def create_item(item: Item):
    print(item.model_dump(exclude={"price"}))
    return item


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
