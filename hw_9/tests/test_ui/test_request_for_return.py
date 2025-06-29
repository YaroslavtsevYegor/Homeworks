import allure
from hw_9.pages.item_page import ItemPage
from hw_9.pages.main_page import MainPage
from hw_9.pages.catalog_page import CatalogPage
from hw_9.pages.shopping_cart_page import ShoppingCartPage
from hw_9.pages.account_page import AccountPage
from hw_9.fixtures.ui_fixtures import user_login


@allure.epic('UI')
@allure.feature('Заказ')
@allure.title('Заявка на возврат ранее заказанного товара')
def test_order_by_user_from_comparison_page(browser, user_login, db_session):
    page = MainPage(browser)
    page.go_to_monitors()
    catalog = CatalogPage(browser)
    catalog.add_to_wishlist()
    page.go_to_wishlist()
    account = AccountPage(browser)
    account.add_to_cart_from_wishlist()
    item_page = ItemPage(browser)
    item_page.choose_available_options()
    page.go_to_cart_checkout()
    ShoppingCartPage(browser).checkout()
    page.go_to_order_history()
    account.view_order()
    result = account.return_order()
    assert 'Product Returns' == result
