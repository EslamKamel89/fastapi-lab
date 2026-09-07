from typing import Any, Literal

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError, create_model

app = FastAPI()


BASE_FIELDS = {
    "sku": (str, ...),
    "price": (float, ...),
}


CATEGORY_DATABASE = {
    1: {
        "name": "Laptop",
        "fields": {
            "cpu": (str, ...),
            "ram": (str, ...),
        },
    },
    2: {
        "name": "TShirt",
        "fields": {
            "color": (str, ...),
            "size": (
                Literal["S", "M", "L", "XL"],
                ...,
            ),
        },
    },
    3: {
        "name": "ManufacturingEquipment",
        "fields": {
            "voltage": (int, ...),
            "warranty_expiration": (str, ...),
        },
    },
}


PRODUCT_DATABASE = {
    101: {
        "category_id": 1,
        "sku": "LAP-101",
        "price": 1200.0,
        "attributes": {
            "cpu": "Intel i7",
            "ram": "16GB",
        },
    },
    202: {
        "category_id": 2,
        "sku": "TS-202",
        "price": 29.99,
        "attributes": {
            "color": "White",
            "size": "L",
        },
    },
    303: {
        "category_id": 3,
        "sku": "EQ-303",
        "price": 4500.0,
        "attributes": {
            "voltage": 220,
            "warranty_expiration": "2028-12-31",
        },
    },
}


def get_product_model(category_id: int) -> type[BaseModel]:
    category = CATEGORY_DATABASE.get(category_id)

    if category is None:
        raise HTTPException(
            status_code=404,
            detail="Product category not found",
        )

    all_fields = {
        **BASE_FIELDS,
        **category["fields"],
    }

    model_name = f"Dynamic{category['name']}Model"

    return create_model(
        model_name,
        **all_fields,
    )


@app.post("/products/{category_id}")
async def create_product(
    category_id: int,
    request_body: dict[str, Any],
):
    ProductModel = get_product_model(category_id)

    try:
        validated_product = ProductModel(
            **request_body,
        )
    except ValidationError as error:
        raise HTTPException(
            status_code=422,
            detail=error.errors(),
        )

    return {
        "message": "Product created successfully",
        "product": validated_product.model_dump(),
    }


@app.get(
    "/products",
    response_model=list[dict[str, Any]],
)
async def get_all_products():
    return list(PRODUCT_DATABASE.values())


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product_data = PRODUCT_DATABASE.get(product_id)

    if product_data is None:
        raise HTTPException(
            status_code=404,
            detail="Product does not exist",
        )

    ResponseModel = get_product_model(
        product_data["category_id"],
    )

    response_data = {
        "sku": product_data["sku"],
        "price": product_data["price"],
        **product_data["attributes"],
    }

    try:
        validated_response = ResponseModel(
            **response_data,
        )
    except ValidationError as error:
        raise HTTPException(
            status_code=422,
            detail=error.errors(),
        )

    return validated_response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
