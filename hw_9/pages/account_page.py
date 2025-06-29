import allure
from hw_9.pages.base_page import BasePage
from hw_9.locators.account_locators import AccountPageLocators


class AccountPage(BasePage):

    @allure.step("Заполнить форму регистрации")
    def registration(self, firstname='Testname', lastname='Testlastname', email='test@test.ru', telephone='21554',
                     password='password', password_confirm='password', timeout=5):
        self.logger.info("%s: Регистрация пользователя" % (self.class_name))
        self.input_value(AccountPageLocators.first_name_field,
                         firstname, timeout)
        self.input_value(AccountPageLocators.last_name_field,
                         lastname, timeout)
        self.input_value(AccountPageLocators.email_field, email, timeout)
        self.input_value(AccountPageLocators.telephone_field,
                         telephone, timeout)
        self.input_value(AccountPageLocators.password_field, password, timeout)
        self.input_value(
            AccountPageLocators.confirm_password_field, password_confirm, timeout)
        self.click(AccountPageLocators.privacy_policy_checkbox, timeout)
        self.click(AccountPageLocators.continue_registration_button, timeout)
        self.click(AccountPageLocators.continue_button, timeout)
        return firstname + ' ' + lastname

    @allure.step("Перейти на страницу редактирования аккаунта")
    def edit_account(self, timeout=5):
        self.logger.info("%s: Открытие страницы редактирования аккаунта пользователя" % (self.class_name))
        self.click(
            AccountPageLocators.edit_account_information_button, timeout)

    @allure.step("Получить данные аккаунта")
    def get_account_personal_details(self, timeout=5):
        self.logger.info("%s: Получение данных об аккаунте" %
                         (self.class_name))
        firstname = self.get_element(
            AccountPageLocators.first_name_field, timeout).get_attribute('value')
        lastname = self.get_element(
            AccountPageLocators.last_name_field, timeout).get_attribute('value')
        email = self.get_element(
            AccountPageLocators.email_field, timeout).get_attribute('value')
        telephone = self.get_element(
            AccountPageLocators.telephone_field, timeout).get_attribute('value')
        return firstname, lastname, email, telephone

    @allure.step("Войти в аккаунт")
    def login_as_returning_customer(self, email='test@test.ru', password='password', timeout=5):
        self.logger.info("%s: Вход в аккаунт пользователя" %
                         (self.class_name))
        self.input_value(AccountPageLocators.email_field, email, timeout)
        self.input_value(AccountPageLocators.password_field, password, timeout)
        self.click(AccountPageLocators.login_as_customer_button, timeout)

    @allure.step("Ввести данные адреса для аккаунта")
    def modify_address_book(self, firstname='Testname', lastname='Testlastname',
                            address_1='Pushkina-Kolotushkina 4',
                            city='Testcity', post_code='123456', country='Antigua and Barbuda',
                            region_state='Barbuda', timeout=5):
        self.logger.info(
            "%s: Добавление нового адреса в адресную книгу пользователя" % (self.class_name))
        self.click(AccountPageLocators.modify_address_button, timeout)
        self.click(AccountPageLocators.new_address_button, timeout)
        self.input_value(AccountPageLocators.first_name_field,
                         firstname, timeout)
        self.input_value(AccountPageLocators.last_name_field,
                         lastname, timeout)
        self.input_value(
            AccountPageLocators.address_1_field, address_1, timeout)
        self.input_value(AccountPageLocators.city_field, city, timeout)
        self.input_value(
            AccountPageLocators.postcode_field, post_code, timeout)
        self.select_from_dropdown(
            AccountPageLocators.country_field, country, timeout)
        self.select_from_dropdown(
            AccountPageLocators.region_state_field, region_state, timeout)
        self.click(AccountPageLocators.default_address_button, timeout)
        self.click(AccountPageLocators.continue_registration_button, timeout)

    @allure.step("Получить данные заказа")
    def get_order_data(self, timeout=5):
        self.logger.info("%s: Получение данных о заказах" % (self.class_name))
        table = self.get_element(
            AccountPageLocators.order_history_table_rows, timeout).text
        return table

    @allure.step("Добавить товар в корзину из списка желаемого")
    def add_to_cart_from_wishlist(self, timeout=5):
        self.logger.info(
            "%s: Добавление товара в корзину из желаемого" % (self.class_name))
        self.get_element(AccountPageLocators.add_to_cart_wishlist, timeout)
        self.click(AccountPageLocators.add_to_cart_wishlist, timeout)

    @allure.step("Посмотреть детали заказа")
    def view_order(self, timeout=5):
        self.logger.info("%s: Просмотр заказов" % (self.class_name))
        self.click(AccountPageLocators.view_order_button, timeout)

    @allure.step("Оформить возврат")
    def return_order(self, telephone='92591590316', timeout=5):
        self.logger.info("%s: Оформление возврата заказа" % (self.class_name))
        self.click(AccountPageLocators.return_order_button, timeout)
        self.input_value(AccountPageLocators.telephone_field,
                         telephone, timeout)
        self.click(AccountPageLocators.return_reason_button, timeout)
        self.click(AccountPageLocators.submit_button, timeout)
        return self.get_element(AccountPageLocators.product_returns_notification, timeout).text
