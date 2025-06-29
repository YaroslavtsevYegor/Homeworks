import allure
from selenium.webdriver.common.action_chains import ActionChains
from hw_9.locators.catalog_locators import CatalogPageLocators
from hw_9.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):

    @allure.step("Добавить товар в корзину из каталога")
    def add_to_cart(self, timeout=5):
        self.logger.info(
            "%s: Нажатие на кнопку 'Добавить в корзину' из каталога" % (self.class_name))
        self.get_element(CatalogPageLocators.add_to_card_button, timeout)
        self.click(CatalogPageLocators.add_to_card_button, timeout)

    @allure.step("Добавить товар в список желаемого из каталога")
    def add_to_wishlist(self, timeout=5):
        self.logger.info("%s: Нажатие на кнопку 'Добавить в желаемое' из каталога" %
                         (self.class_name))
        elements = self.get_elements(
            CatalogPageLocators.add_to_wish_list_button, timeout)
        for e in elements:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(e))
            ActionChains(self.browser).move_to_element(
                e).pause(1).click().perform()
            self.get_element(CatalogPageLocators.success_alert, timeout)
            WebDriverWait(e._parent, timeout).until(
                lambda driver: driver.execute_script(
                    "return document.readyState") == "complete"
            )


    @allure.step("Добавить товары к сравнению из каталога")
    def add_to_compare(self, timeout=5):
        self.logger.info("%s: Нажатие на кнопку 'Добавить к сравнению' из каталога" %
                         (self.class_name))
        elements = self.get_elements(
            CatalogPageLocators.compare_this_product_button, timeout)
        for e in elements:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(e))
            e.click()
            self.get_element(CatalogPageLocators.success_alert, timeout)
            WebDriverWait(e._parent, timeout).until(
                lambda driver: driver.execute_script(
                    "return document.readyState") == "complete"
            )

    @allure.step("Добавить товар к сравнению из каталога")
    def add_product_to_compare(self, timeout=5):
        self.logger.info("%s: Добавление товара к сравнению" %
                         (self.class_name))
        self.get_element(CatalogPageLocators.compare_samsung_tab_button, timeout)
        self.click(
            CatalogPageLocators.compare_samsung_tab_button, timeout)
        self.get_element(CatalogPageLocators.success_alert, timeout)

    @allure.step("Перейти на страницу сравнения из каталога")
    def go_to_product_comparison(self, timeout=5):
        self.logger.info("%s: Переход на страницу сравнения из каталога" %
                         (self.class_name))
        self.get_element(CatalogPageLocators.product_compare_button, timeout)
        self.click(CatalogPageLocators.product_compare_button, timeout)
