import pytest

from hw_6.pages.admin_dashboard_page import DashboardPage

from hw_6.fixtures.login_fixtures import admin_login
from hw_6.fixtures.products_action_fixtures import temp_product_for_add


def test_add_product(browser, admin_login, temp_product_for_add):
    page = DashboardPage(browser)
    page.choose_catalog_tab()
    page.choose_products_tab()
    product_name = page.add_new_product(**temp_product_for_add)
    result_search = page.search_result(**temp_product_for_add)
    assert product_name in result_search
