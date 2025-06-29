import allure
from hw_9.pages.main_page import MainPage
from hw_9.pages.item_page import ItemPage
from hw_9.pages.shopping_cart_page import ShoppingCartPage
from hw_9.pages.account_page import AccountPage
from hw_9.pages.catalog_page import CatalogPage


@allure.epic('UI')
@allure.feature('Регистрация')
@allure.title('Регистрация пользователя при оформлении товара')
def test_register_new_user_during_checkout(browser, db_session):
    page = MainPage(browser)
    page.go_to_cameras_catalog()
    CatalogPage(browser).add_to_cart()
    item_page = ItemPage(browser)
    item_page.select_color()
    item_page.fill_in_quantity()
    item_page.add_to_cart()
    page.go_to_shopping_cart()
    shopping_page = ShoppingCartPage(browser)
    shopping_page.click_checkout()
    shopping_page.choose_register_account_option()
    input_fields = shopping_page.fill_registration_form()
    shopping_page.refresh_page()
    page.go_to_my_account()
    account_page = AccountPage(browser)
    account_page.edit_account()
    written_fields = account_page.get_account_personal_details()
    assert input_fields == written_fields
