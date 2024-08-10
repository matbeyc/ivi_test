from pydantic import BaseModel, RootModel


class Chocolate(BaseModel):
    id: int
    name: str
    price: float


class Chocolates(RootModel):
    root: list[Chocolate]


class ChocolatePrice(BaseModel):
    price: float


class Error(BaseModel):
    error: str


class SuccessPurchase(BaseModel):
    message: str
    balance: float
