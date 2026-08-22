import json
from typing import Annotated

import uvicorn
from fastapi import Body, Depends, FastAPI, Header, HTTPException, Path
from pydantic import BaseModel, Field, StringConstraints, validate_call
from pydantic_core._pydantic_core import ValidationError

app = FastAPI()


def get_db_session():
    print("DB Session started")
    db = {
        1: {"name": "item 1"},
        2: {"name": "item 2"},
    }
    try:
        yield db
    finally:
        print("DB session tear down")


DBSession = Annotated[dict[int, dict[str, str]], Depends(get_db_session)]


async def get_user(
    token: Annotated[str | None, Header()] = None,
):
    print("Checking user")
    return {"username": token or "Eslam Kamel"}


User = Annotated[dict[str, str], Depends(get_user)]


@app.get("/item/{item_id}")
async def read_item(item_id: Annotated[int, Path(g=0)], db: DBSession, user: User):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": db.get(item_id, {}), "user": user}


class ItemCreate(BaseModel):
    name: str
    price: float | None = None


@app.post("/item")
async def create_item(
    item: ItemCreate,
    db: DBSession,
    user: User,
):
    new_id = max(db.keys()) + 1
    db[new_id] = {"name": item.name}
    return item


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
