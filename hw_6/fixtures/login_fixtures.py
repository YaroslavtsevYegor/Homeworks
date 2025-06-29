import pytest
import os
from dotenv import load_dotenv

load_dotenv()
from hw_6.pages.admin_login_page import AdministrationLoginPage


@pytest.fixture(params=[{
    'username': os.getenv("admin_login"),
    'password': os.getenv("admin_password")
}
])
def admin_login(browser, request):
    page = AdministrationLoginPage(browser)
    page.login(**request.param)
    yield page
