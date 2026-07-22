from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"messege": "Hello, World!"}


@app.get("/greet/{name}")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello, {name}!"}


@app.get("/book")
async def get_book(slug: str) -> dict:
    name = slug.replace("-", " ").capitalize()
    return {"book": name}


class Book(BaseModel):
    title: str
    author: str
    price: float
    is_availiable: bool = True


@app.post("/book")
def create_item(book: Book) -> dict:
    return {"message": "Item created", "data": book}
