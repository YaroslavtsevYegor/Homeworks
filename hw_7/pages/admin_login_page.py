import allure
from selenium.webdriver.common.by import By
from hw_7.pages.base_page import BasePage


class AdministrationLoginPage(BasePage):
    login_admin_form = By.XPATH, '//form'
    login_admin_username = By.NAME, 'username'
    login_admin_password = By.NAME, 'password'
    login_button = By.XPATH, '//button[contains(text(),"Login")]'

    @allure.step("Login as admin")
    def login(self, username, password, timeout=3):
        self.open("administration")
        self.logger.info("%s: Fill admin authentication form" % (self.class_name))
        self.click(self.login_button, timeout)
        form = self.get_element(self.login_admin_form, timeout)
        self.input_value(self.login_admin_username, username, timeout)
        self.input_value(self.login_admin_password, password, timeout)
        form.submit()
