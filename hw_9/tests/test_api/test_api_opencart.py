import json
import allure
from hw_9.models.api_models import CartModifyResponse, CurrencyModifyResponse, DataModel, VouchersContainer
from sqlalchemy import select
import requests
import pytest
from hw_9.fixtures.api_fixtures import add_temp_product, get_cart
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("api_url")
cart_add_url = os.getenv("api_url_cart_add")
cart_edit_url = os.getenv("api_url_cart_edit")
cart_remove_url = os.getenv("api_url_cart_remove")
currency_url = os.getenv("api_url_currency")
cart_get_url = os.getenv("api_url_cart_products")
voucher_add_url = os.getenv("api_url_voucher_add")


@allure.epic('API')
@allure.feature('Корзина')
@allure.story('Добавить')
@allure.title('Добавить товар в корзину')
@pytest.mark.parametrize("product_id,quantity",
                         [('28', '1')])
def test_add_product_to_card(api_token, product_id, quantity, db_session):
    response = requests.post(
        f'{base_url}{cart_add_url}',
        params={'api_token': api_token},
        data={
            'product_id': product_id,
            'quantity': quantity
        })
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        CartModifyResponse.model_validate(response.json())
    session, oc_cart, oc_session = db_session
    stmt = select(oc_cart).where((oc_cart.c.session_id == api_token) &
                                 (oc_cart.c.product_id == product_id) &
                                 (oc_cart.c.quantity == quantity))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchone()
    with allure.step("Проверка таблицы oc_cart в базе данных"):
        assert result, "Корзина пустая"


@allure.epic('API')
@allure.feature('Корзина')
@allure.story('Изменить')
@allure.title('Изменить количество ранее добавленного товара в корзине')
@pytest.mark.parametrize("quantity",
                         [('4')])
def test_change_quantity_at_card(add_temp_product, api_token, quantity, db_session):
    cart_id = add_temp_product
    response = requests.post(
        f'{base_url}{cart_edit_url}',
        params={'api_token': api_token},
        data={
            'key': cart_id,
            'quantity': quantity
        })
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        CartModifyResponse.model_validate(response.json())
    session, oc_cart, oc_session = db_session
    stmt = select(oc_cart.c.quantity).where(
        (oc_cart.c.session_id == api_token))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchone()
    with allure.step("Проверка таблицы oc_cart в базе данных"):
        assert int(quantity) in result


@allure.epic('API')
@allure.feature('Корзина')
@allure.story('Удалить')
@allure.title('Удалить ранее добавленный товар из корзины')
def test_remove_product_from_card(add_temp_product, api_token, db_session):
    cart_id = add_temp_product
    response = requests.post(
        f'{base_url}{cart_remove_url}',
        params={'api_token': api_token},
        data={
            'key': cart_id,
        })
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        CartModifyResponse.model_validate(response.json())
    session, oc_cart, oc_session = db_session
    stmt = select(oc_cart).where(
        (oc_cart.c.session_id == api_token))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchone()
    with allure.step("Проверка таблицы oc_cart в базе данных"):
        assert result[0] != cart_id, "Корзина не пустая"


@allure.epic('API')
@allure.feature('Корзина')
@allure.story('Просмотреть')
@allure.title('Получить содержимое корзины')
def test_get_card(api_token, add_temp_product):
    response = requests.post(
        f'{base_url}{cart_get_url}',
        params={'api_token': api_token},
        data={}
    )
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        DataModel.model_validate(response.json())


@allure.epic('API')
@allure.feature('Валюта')
@allure.story('Переключить')
@allure.title('Изменения валюты для сессии')
@pytest.mark.parametrize("currency",
                         ('EUR', 'USD', 'GBP'))
def test_currency_switch(api_token, add_temp_product, db_session, currency, get_cart):
    response = requests.post(
        f'{base_url}{currency_url}',
        params={'api_token': api_token},
        data={
            'currency': currency,
        })
    if currency == 'EUR':
        currency_sign = '€'
    elif currency == 'USD':
        currency_sign = '$'
    elif currency == 'GBP':
        currency_sign = '£'
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        CurrencyModifyResponse.model_validate(response.json())
    cart_json = get_cart(api_token)
    cart_totals = cart_json['totals']
    texts_at_cart_totals = [item['text'] for item in cart_totals]
    with allure.step("Проверка текущей корзины"):
        for price in texts_at_cart_totals:
            assert currency_sign in price
    session, oc_cart, oc_session = db_session
    stmt = select(oc_session.c.data).where(
        (oc_session.c.session_id == api_token))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchone()
    with allure.step("Проверка таблицы oc_session в базе данных"):
        assert currency in result[0]


@allure.epic('API')
@allure.feature('Ваучер')
@allure.story('Добавить')
@allure.title('Добавление ваучера в корзину для сессии')
def test_add_voucher(api_token, add_temp_product, db_session, get_cart):
    response = requests.post(
        f'{base_url}{voucher_add_url}',
        params={'api_token': api_token},
        data={
            'from_name': 'MyOpenCart Admin',
            'from_email': 'admin@example.com',
            'to_name': 'Dear Customer',
            'to_email': 'customer@example.com',
            'amount': '10',
            'code': '1234',
            "message": "gift voucher"
        })
    with allure.step("Отправлен запрос, проверка кода ответа"):
        assert response.status_code == 200, f"Некорректный код ответа, получен {response.status_code}"
    with allure.step("Валидация ответа"):
        CartModifyResponse.model_validate(response.json())
    session, oc_cart, oc_session = db_session
    stmt = select(oc_session.c.data).where(
        (oc_session.c.session_id == api_token))
    result_proxy = session.execute(stmt)
    result = result_proxy.fetchone()
    json_str = result[0]
    data_json = json.loads(json_str)
    with allure.step("Проверка таблицы oc_session в базе данных"):
        assert data_json['vouchers'], 'Ваучер пустой'
    cart_json = get_cart(api_token)
    cart_vouchers = cart_json['vouchers']
    with allure.step("Проверка текущей корзины"):
        VouchersContainer.model_validate({'vouchers': cart_vouchers})
