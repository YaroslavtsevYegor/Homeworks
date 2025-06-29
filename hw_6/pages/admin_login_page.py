from selenium.webdriver.common.by import By

from hw_6.pages.base_page import BasePage


class AdministrationLoginPage(BasePage):
    login_admin_form = By.XPATH, '//form'
    login_admin_username = By.NAME, 'username'
    login_admin_password = By.NAME, 'password'

    def login(self, username, password,timeout=1):
        self.open("administration")
        form = self.get_element(self.login_admin_form,timeout)
        self.input_value(self.login_admin_username, username,timeout)
        self.input_value(self.login_admin_password, password,timeout)
        form.submit()
