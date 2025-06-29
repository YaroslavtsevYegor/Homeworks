import allure
from hw_9.pages.base_page import BasePage
from hw_9.locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self, timeout=5):
        self.logger.info("%s: Нажатие на кнопку 'Checkout'" % (self.class_name))
        self.click(ShoppingCartPageLocators.checkout_button, timeout)

    @allure.step("Выбрать опцию 'Register Account'")
    def choose_register_account_option(self, timeout=5):
        self.logger.info(
            "%s: Выбор опции регистрации нового аккаунта при оформлении заказа" % (self.class_name))
        self.click(
            ShoppingCartPageLocators.register_account_radio_button, timeout)
        self.click(
            ShoppingCartPageLocators.continue_registration_account_button, timeout)

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, firstname='Testname', lastname='Testlastname', email='test@test.ru',
                               address_1='Pushkina-Kolotushkina 4', telephone='21554',
                               city='Testcity', post_code='123456', country='Antigua and Barbuda',
                               region_state='Barbuda', password='password', password_confirm='password', timeout=5):
        self.logger.info(
            "%s: Заполнение формы регистрации пользователя" % (self.class_name))
        self.input_value(
            ShoppingCartPageLocators.first_name_field, firstname, timeout)
        self.input_value(
            ShoppingCartPageLocators.lastname_name_field, lastname, timeout)
        self.input_value(ShoppingCartPageLocators.email_field, email, timeout)
        self.input_value(
            ShoppingCartPageLocators.telephone_field, telephone, timeout)
        self.input_value(
            ShoppingCartPageLocators.address_1_field, address_1, timeout)
        self.input_value(ShoppingCartPageLocators.city_field, city, timeout)
        self.input_value(
            ShoppingCartPageLocators.postcode_field, post_code, timeout)
        self.select_from_dropdown(
            ShoppingCartPageLocators.country_field, country, timeout)
        self.select_from_dropdown(
            ShoppingCartPageLocators.region_state_field, region_state, timeout)
        self.input_value(
            ShoppingCartPageLocators.password_field, password, timeout)
        self.input_value(
            ShoppingCartPageLocators.password_confirm_field, password_confirm, timeout)
        self.click(ShoppingCartPageLocators.privacy_policy_checkbox, timeout)
        self.get_element(
            ShoppingCartPageLocators.continue_registration_button, timeout)
        self.click(ShoppingCartPageLocators.continue_registration_button, timeout)
        self.get_element(
            ShoppingCartPageLocators.delivery_method_continue_button, timeout)
        return firstname, lastname, email, telephone

    @allure.step("Удалить товар из корзины")
    def remove_from_cart(self, timeout=5):
        self.logger.info("%s: Нажатие кнопки 'Remove'" % (self.class_name))
        self.click(
            ShoppingCartPageLocators.remove_from_shopping_cart_button, timeout)

    @allure.step("Изменить количество товара в корзине")
    def change_quantity(self, qty='2', timeout=5):
        self.logger.info("%s: Ввод в поле 'Quantity' значения %s и нажатие кнопки 'Update'" % (
            self.class_name, qty))
        self.get_element(ShoppingCartPageLocators.quantity_field, timeout)
        self.input_value(ShoppingCartPageLocators.quantity_field, qty, timeout)
        self.click(ShoppingCartPageLocators.update_quantity_button, timeout)
        self.get_element(ShoppingCartPageLocators.success_alert, timeout)

    @allure.step("Заполнить форму оценки стоимости доставки и налогов")
    def estimate_shipping_taxes(self, post_code='123456', country='Antigua and Barbuda',
                               region_state='Barbuda', timeout=5):
        self.logger.info(
            "%s: Ввод данных в форму отправки заказа" % (self.class_name))
        self.click(ShoppingCartPageLocators.shipping_taxes_section, timeout)
        self.input_value(
            ShoppingCartPageLocators.shipping_taxes_postcode_field, post_code, timeout)
        self.select_from_dropdown(
            ShoppingCartPageLocators.shipping_taxes_country_field, country, timeout)
        self.select_from_dropdown(
            ShoppingCartPageLocators.shipping_taxes_region_state_field, region_state, timeout)
        self.click(ShoppingCartPageLocators.get_quotes_button, timeout)
        self.click(ShoppingCartPageLocators.cancel_button, timeout)

    @allure.step("Продолжить оформление и подтвердить заказ")
    def checkout(self, comment='Will buy soon', timeout=5):
        self.logger.info("%s: Продолжение оформления заказа, оставление комментария %s и подтверждение заказа" % (
            self.class_name, comment))
        self.click(ShoppingCartPageLocators.checkout_button, timeout)
        self.click(ShoppingCartPageLocators.billing_continue_button, timeout)
        self.click(ShoppingCartPageLocators.delivery_continue_button, timeout)
        self.input_value(
            ShoppingCartPageLocators.delivery_method_comment, comment, timeout)
        self.click(
            ShoppingCartPageLocators.delivery_method_continue_button, timeout)
        self.click(ShoppingCartPageLocators.terms_conditions_checkbox, timeout)
        self.click(ShoppingCartPageLocators.payment_continue_button, timeout)
        self.click(ShoppingCartPageLocators.confirm_order, timeout)
        self.click(ShoppingCartPageLocators.continue_button, timeout)
