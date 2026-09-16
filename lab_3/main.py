from api.product import router as product_router
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
