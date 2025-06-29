import pytest
import requests
from sqlalchemy import select
import allure
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("api_url")
cart_add_url = os.getenv("api_url_cart_add")
cart_get_url = os.getenv("api_url_cart_products")


@allure.title('Добавить продукт в корзину')
@pytest.fixture(params=[{'product_id': '29', 'quantity': '1'}])
def add_temp_product(api_token, db_session, request):
    response = requests.post(
        f'{base_url}{cart_add_url}',
        params={'api_token': api_token},
        data=request.param
    )
    session, oc_cart, oc_session = db_session
    stmt = select(oc_cart.c.cart_id).where((oc_cart.c.session_id == api_token))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchall()
    session.commit()
    return str(result[0][0])


@allure.title('Просмотреть корзину')
@pytest.fixture
def get_cart():
    def _get_cart(api_token):
        response = requests.post(
            f'{base_url}{cart_get_url}',
            params={'api_token': api_token},
            data={}
        )
        return response.json()

    return _get_cart
