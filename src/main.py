from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from user.models import start_mapper as start_user_mapper
from user.routes import router as user_router


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    start_user_mapper()
    fastapi_app.include_router(user_router)
    yield
    clear_mappers()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
