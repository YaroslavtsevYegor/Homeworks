import allure
import pytest
from hw_9.pages.main_page import MainPage
from hw_9.pages.account_page import AccountPage


@allure.title('Зарегистрировать пользователя и выйти')
@pytest.fixture
def register_new_user(browser):
    page = MainPage(browser)
    page.go_to_registration()
    account_page = AccountPage(browser)
    user_details = account_page.registration()
    account_page.modify_address_book()
    page.logout()
    page.open_main_page()
    return user_details


@allure.title('Зарегистрировать пользователя')
@pytest.fixture
def user_login(browser):
    page = MainPage(browser)
    page.go_to_registration()
    account_page = AccountPage(browser)
    user_details = account_page.registration()
    account_page.modify_address_book()
    page.open_main_page()
    return user_details
