from selenium.webdriver.common.by import By

from hw_6.pages.base_page import BasePage


class DashboardPage(BasePage):
    catalog_tab = By.XPATH, "//a[contains(text(),'Catalog')]"
    products_tab = By.XPATH, "//a[contains(text(),'Products')]"
    add_new_product_button = By.XPATH, "//div[@class='float-end']/child::a"
    product_name_field = By.ID, "input-name-1"
    meta_tag_title_field = By.ID, "input-meta-title-1"
    data_tab = By.XPATH, "//a[contains(text(),'Data')]"
    model_field = By.ID, 'input-model'
    seo_tab = By.XPATH, "//a[text()='SEO']"
    keyword_field = By.XPATH, "//input[@placeholder='Keyword']"
    save_new_product_button = By.XPATH, "//div[@class='float-end']/child::button"
    product_name_filter_field = By.ID, "input-name"
    filter_button = By.ID, "button-filter"
    select_filtered_product = By.XPATH, "//input[@name='selected[]']"
    delete_product_button = By.XPATH, "//button[@title='Delete']"
    filtered_field = By.XPATH, '//tbody'

    def choose_catalog_tab(self, timeout=1):
        self.click(self.catalog_tab, timeout)

    def choose_products_tab(self, timeout=1):
        self.click(self.products_tab, timeout)

    def add_new_product(self, product_name, product_tag, product_model, product_keyword, timeout=1):
        self.click(self.add_new_product_button, timeout)
        self.input_value(self.product_name_field, product_name, timeout)
        self.input_value(self.meta_tag_title_field, product_tag, timeout)
        self.click(self.data_tab, timeout)
        self.input_value(self.model_field, product_model, timeout)
        self.click(self.seo_tab, timeout)
        self.input_value(self.keyword_field, product_keyword, timeout)
        self.click(self.save_new_product_button, timeout)
        return product_name

    def delete_product(self, product_name, product_tag, product_model, product_keyword, timeout=1):
        self.input_value(self.product_name_filter_field, product_name, timeout)
        self.click(self.filter_button, timeout)
        self.click(self.select_filtered_product, timeout)
        self.click(self.delete_product_button, timeout)
        alert = self.browser.switch_to.alert
        alert.accept()
        return product_name

    def search_result(self, product_name, product_tag, product_model, product_keyword, timeout=1):
        self.choose_products_tab()
        self.input_value(self.product_name_filter_field, product_name, timeout)
        self.click(self.filter_button, timeout)
        result_text = self.get_element(self.filtered_field, timeout)
        return result_text.get_attribute('innerText')
