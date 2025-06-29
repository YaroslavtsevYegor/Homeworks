from selenium.webdriver.common.by import By
from hw_7.pages.base_page import BasePage


class MainPage(BasePage):
    account_button = By.XPATH, '//span[contains(text(),"My Account")]'
    register_button = By.XPATH, "//a[contains(text(),'Register')]"
    currency_dropdown = By.ID, 'form-currency'
    currency_option = By.XPATH, "//a[contains(text(),'{}')]"
    currency_list = By.XPATH, "//ul[@class='dropdown-menu show']/child::li"

    def move_to_registration(self, timeout=1):
        self.logger.info("%s: Go to registration page" % (self.class_name))
        self.click(self.account_button, timeout)
        self.click(self.register_button, timeout)

    def select_currency(self, currency_name, timeout=10):
        self.logger.info("%s: Selecting currency" % (self.class_name))
        self.click(self.currency_dropdown, timeout)
        self.click((self.currency_option[0], self.currency_option[1].format(currency_name)), timeout)

    def get_current_currency(self, timeout=10):
        self.logger.info("%s: Getting current currency" % (self.class_name))
        return self.get_element(self.currency_dropdown, timeout).text.split()[0]
