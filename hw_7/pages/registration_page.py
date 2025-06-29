import allure
from selenium.webdriver.common.by import By
from hw_7.pages.base_page import BasePage


class RegistrationPage(BasePage):
    registration_form = By.ID, 'form-register'
    firstname_field = By.NAME, 'firstname'
    lastname_field = By.NAME, 'lastname'
    email_field = By.NAME, 'email'
    password_field = By.NAME, 'password'
    privacy_policy_switch = By.NAME, 'agree'
    continue_button = By.XPATH, '//a[contains(text(),"Continue")]'

    @allure.step("Register new user")
    def registration(self, firstname, lastname, email, password, timeout=1):
        self.logger.info("%s: Fill user registration form" % (self.class_name))
        form = self.get_element(self.registration_form, timeout)
        self.input_value(self.firstname_field, firstname, timeout)
        self.input_value(self.lastname_field, lastname, timeout)
        self.input_value(self.email_field, email, timeout)
        self.input_value(self.password_field, password, timeout)
        self.click(self.privacy_policy_switch, timeout)
        form.submit()
        return self.get_element(self.continue_button, timeout)
