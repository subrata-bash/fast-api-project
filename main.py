from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    return {"data": 'All Posts is here'}


@app.post("/createposts")
def create_post(new_post: Post):
    print(new_post)
    return {"data": new_post}
