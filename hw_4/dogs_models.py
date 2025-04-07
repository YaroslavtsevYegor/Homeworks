from pydantic import BaseModel


class DogImageResponse(BaseModel):
    message: str
    status: str


class DogImagesResponse(BaseModel):
    message: list
    status: str


class DogBreedsResponse(BaseModel):
    message: dict
    status: str
