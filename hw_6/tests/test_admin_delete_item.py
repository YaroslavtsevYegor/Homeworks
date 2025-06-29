import pytest

from hw_6.pages.admin_dashboard_page import DashboardPage

from hw_6.fixtures.login_fixtures import admin_login
from hw_6.fixtures.products_action_fixtures import temp_product_for_delete


def test_delete_product(browser, admin_login, temp_product_for_delete):
    page = DashboardPage(browser)
    page.choose_products_tab()
    product_name = page.delete_product(**temp_product_for_delete)
    result_search = DashboardPage(browser).search_result(**temp_product_for_delete)
    assert product_name not in result_search
