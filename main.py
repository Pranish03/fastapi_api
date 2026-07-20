from fastapi import FastAPI

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
