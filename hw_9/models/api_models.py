from pydantic import BaseModel
from typing import List, Optional, Union
from pydantic import BaseModel


class TotalItem(BaseModel):
    title: str
    text: str


class ProductItem(BaseModel):
    cart_id: Union[str, int]
    product_id: Union[str, int]
    name: str
    model: str
    option: Optional[List] = None
    quantity: str
    stock: bool
    shipping: str
    price: str
    total: str
    reward: Optional[Union[str, int]] = None


class VoucherItem(BaseModel):
    code: int
    description: str
    from_name: str
    from_email: str
    to_name: str
    to_email: str
    voucher_theme_id: str
    message: str
    price: str
    amount: float


class VouchersContainer(BaseModel):
    vouchers: List[VoucherItem]


class DataModel(BaseModel):
    products: List[ProductItem]
    vouchers: List[VoucherItem]
    totals: List[TotalItem]


class LoginResponse(BaseModel):
    success: str = 'Success: API session successfully started!'
    api_token: str


class CartModifyResponse(BaseModel):
    success: str = "Success: You have modified your shopping cart!"


class CurrencyModifyResponse(BaseModel):
    success: str = "Success: Your currency has been changed!"
