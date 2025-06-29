import allure
from hw_9.pages.base_page import BasePage
from hw_9.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self, timeout=5):
        self.logger.info("%s:Нажатие на 'Opencart' и переход на главную страницу" % (self.class_name))
        self.get_element(MainPageLocators.opencart_img, timeout)
        self.click(MainPageLocators.opencart_img, timeout)

    @allure.step("Перейти на страницу 'My account'")
    def go_to_my_account(self, timeout=5):
        self.logger.info(
            "%s: Переход на страницу аккаунта" % (self.class_name))
        self.get_element(MainPageLocators.my_account_dropdown, timeout)
        self.click(MainPageLocators.my_account_dropdown, timeout)
        self.get_element(MainPageLocators.my_account_button, timeout)
        self.click(MainPageLocators.my_account_button, timeout)

    @allure.step("Перейти на страницу 'Registration'")
    def go_to_registration(self, timeout=5):
        self.logger.info("%s: Переход на страницу регистрации" % (self.class_name))
        self.get_element(MainPageLocators.my_account_dropdown, timeout)
        self.click(MainPageLocators.my_account_dropdown, timeout)
        self.get_element(MainPageLocators.register_button, timeout)
        self.click(MainPageLocators.register_button, timeout)

    @allure.step("Перейти на страницу 'Login'")
    def go_to_login(self, timeout=5):
        self.logger.info("%s: Переход на страницу входа в аккаунт" % (self.class_name))
        self.click(MainPageLocators.my_account_dropdown, timeout)
        self.click(MainPageLocators.login_button, timeout)

    @allure.step("Перейти на страницу 'Orders'")
    def go_to_order_history(self, timeout=5):
        self.logger.info("%s: Переход на страницу истории заказов" % (self.class_name))
        self.click(MainPageLocators.my_account_dropdown, timeout)
        self.click(MainPageLocators.order_history_button, timeout)

    @allure.step("Выйти из аккаунта")
    def logout(self, timeout=5):
        self.logger.info("%s: Выход из аккаунта" % (self.class_name))
        self.click(MainPageLocators.my_account_dropdown, timeout)
        self.click(MainPageLocators.logout_button, timeout)

    @allure.step("Перейти на страницу 'Cameras'")
    def go_to_cameras_catalog(self, timeout=5):
        self.logger.info("%s: Переход в каталог 'Cameras'" % (self.class_name))
        self.get_element(MainPageLocators.cameras_tab, timeout)
        self.click(MainPageLocators.cameras_tab, timeout)

    @allure.step("Перейти на страницу 'Phones & PDAs'")
    def go_to_smartphones_catalog(self, timeout=5):
        self.logger.info("%s: Переход в каталог 'Phones & PDAs'" % (self.class_name))
        self.click(MainPageLocators.smartphones_tab, timeout)

    @allure.step("Перейти на страницу 'Monitors'")
    def go_to_monitors(self, timeout=5):
        self.logger.info("%s: Переход в каталог 'Monitors'" % (self.class_name))
        self.click(
            MainPageLocators.components_dropdown, timeout)
        self.get_element(MainPageLocators.monitors_option, timeout)
        self.click(MainPageLocators.monitors_option, timeout)

    @allure.step("Перейти на страницу 'Wish List'")
    def go_to_wishlist(self, timeout=5):
        self.logger.info("%s: Переход в 'Список желаемого'" % (self.class_name))
        self.click(MainPageLocators.wishlist_button, timeout)

    @allure.step("Перейти на страницу 'Checkout'")
    def go_to_cart_checkout(self, timeout=5):
        self.logger.info("%s: Переход к оформлению заказа" % (self.class_name))
        self.get_element(MainPageLocators.cart_button, timeout)
        self.click(MainPageLocators.cart_button, timeout)
        self.get_element(MainPageLocators.checkout_cart_button, timeout)
        self.click(MainPageLocators.checkout_cart_button, timeout)

    @allure.step("Ввести в поле поиска {request} и нажать 'Поиск'")
    def search(self, request='Samsung', timeout=5):
        self.logger.info("%s: Поиск значения %s по сайту" %
                         (self.class_name, request))
        self.input_value(MainPageLocators.search_field,
                         request, timeout)
        self.click(MainPageLocators.search_button, timeout)

    @allure.step("Перейти на страницу 'Shopping cart'")
    def go_to_shopping_cart(self, timeout=5):
        self.logger.info("%s: Переход в 'Корзину'" % (self.class_name))
        self.get_element(MainPageLocators.shopping_cart_button, timeout)
        self.click(MainPageLocators.shopping_cart_button, timeout)
