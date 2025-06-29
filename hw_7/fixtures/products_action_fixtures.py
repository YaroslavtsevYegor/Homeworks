import pytest
import os
from dotenv import load_dotenv
from hw_7.pages.admin_dashboard_page import DashboardPage

load_dotenv()


@pytest.fixture(params=[
    {'product_name': os.getenv("test_product_name"), 'product_tag': os.getenv("test_product_tag"),
     'product_model': os.getenv("test_product_model"),
     'product_keyword': os.getenv("test_product_keyword")}])
def temp_product_for_add(browser, request):
    yield request.param
    DashboardPage(browser).delete_product(**request.param)


@pytest.fixture(params=[
    {'product_name': os.getenv("test_product_name"), 'product_tag': os.getenv("test_product_tag"),
     'product_model': os.getenv("test_product_model"),
     'product_keyword': os.getenv("test_product_keyword")}])
def temp_product_for_delete(browser, request):
    DashboardPage(browser).choose_catalog_tab()
    DashboardPage(browser).choose_products_tab()
    DashboardPage(browser).add_new_product(**request.param)
    yield request.param
