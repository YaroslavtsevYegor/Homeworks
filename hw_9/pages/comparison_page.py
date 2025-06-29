from hw_9.locators.comparison_locators import ComparisonPageLocators
from hw_9.pages.base_page import BasePage
import allure


class ComparisonPage(BasePage):

    @allure.step("Удалить товар из сравнения")
    def remove_from_comparison(self, timeout=5):
        self.logger.info("%s: Удаление товара из списка сравнения" %
                         (self.class_name))
        self.click(ComparisonPageLocators.remove_from_comparison_button, timeout)

    @allure.step("Добавить товар в корзину из сравнения")
    def add_products_to_cart_from_comparison(self, timeout=5):
        self.logger.info(
            "%s: Добавление товара в корзину из списка сравнения" % (self.class_name))
        products = self.get_elements(
            ComparisonPageLocators.add_to_cart_from_comparison_button, timeout)
        products[0].click()
        products[1].click()
