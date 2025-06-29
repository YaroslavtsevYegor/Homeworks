import allure
from hw_9.pages.main_page import MainPage
from hw_9.pages.catalog_page import CatalogPage
from hw_9.pages.shopping_cart_page import ShoppingCartPage
from hw_9.pages.comparison_page import ComparisonPage
from hw_9.pages.account_page import AccountPage
from hw_9.fixtures.ui_fixtures import register_new_user


@allure.epic('UI')
@allure.feature('Заказ')
@allure.title('Оформление заказа авторизованным пользователем со страницы сравнения')
def test_order_from_comparison_page(browser, register_new_user, db_session):
    page = MainPage(browser)
    page.go_to_login()
    account = AccountPage(browser)
    account.login_as_returning_customer()
    page.go_to_smartphones_catalog()
    catalog = CatalogPage(browser)
    catalog.add_to_compare()
    page.search()
    catalog.add_product_to_compare()
    catalog.go_to_product_comparison()
    comparison = ComparisonPage(browser)
    comparison.remove_from_comparison()
    comparison.add_products_to_cart_from_comparison()
    page.go_to_shopping_cart()
    cart = ShoppingCartPage(browser)
    cart.remove_from_cart()
    cart.change_quantity()
    cart.estimate_shipping_taxes()
    cart.checkout()
    page.go_to_order_history()
    result_order = account.get_order_data()
    assert register_new_user in result_order
