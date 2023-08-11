from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from auth import router as auth_router
from config import middlewareKey

app = FastAPI()

secret_key = middlewareKey
app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
