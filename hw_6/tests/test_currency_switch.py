import pytest
import os
from dotenv import load_dotenv

load_dotenv()
from hw_6.pages.main_page import MainPage


@pytest.mark.parametrize("new_currency",
                         [os.getenv("test_currency_euro"), os.getenv("test_currency_pound")])
def test_currency_switch(browser, new_currency):
    page = MainPage(browser)
    old_currency = page.get_current_currency()
    page.select_currency(new_currency)
    assert old_currency != page.get_current_currency()
