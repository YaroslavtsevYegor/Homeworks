from pydantic import BaseModel


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
