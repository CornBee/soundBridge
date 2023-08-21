from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from routes import router
from config import middlewareKey

from test import insert_test_data

app = FastAPI()

secret_key = middlewareKey
app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/profile")
def read_root():
    return {"This is": "Profile Page"}


if __name__ == "__main__":
    import uvicorn
    insert_test_data()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
