import pytest
import os
from dotenv import load_dotenv

load_dotenv()
from hw_6.pages.main_page import MainPage
from hw_6.pages.registration_page import RegistrationPage


@pytest.mark.parametrize("firstname,lastname,email,password",
                         [(os.getenv("test_username_firstname"), os.getenv("test_username_lastname"),
                           os.getenv("test_username_email"), os.getenv("test_username_password"))])
def test_register_new_user(browser, firstname, lastname, email, password):
    MainPage(browser).move_to_registration()
    registration = RegistrationPage(browser).registration(firstname, lastname, email, password)
    assert registration.is_displayed()
