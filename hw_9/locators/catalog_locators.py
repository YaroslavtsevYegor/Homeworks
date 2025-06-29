from selenium.webdriver.common.by import By


class CatalogPageLocators(object):
    add_to_card_button = By.XPATH, "//span[contains(text(),'Add to Cart')]"
    product_compare_button = By.XPATH, "//a[contains(text(),'Product Compare')]"
    compare_this_product_button = By.XPATH, "//button[@data-original-title='Compare this Product']"
    add_to_wish_list_button = By.XPATH, "//button[@data-original-title='Add to Wish List']"
    search_field = By.XPATH, "//input[@name='search']"
    search_button = By.XPATH, "//i[@class='fa fa-search']"
    success_alert = By.XPATH, "//div[contains(text(),'Success')]"
    compare_samsung_tab_button = By.XPATH, "//button[@onclick=\"compare.add('49');\"]"
