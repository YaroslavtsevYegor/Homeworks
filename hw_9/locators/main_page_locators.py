from selenium.webdriver.common.by import By


class MainPageLocators(object):
    register_button = By.XPATH, "//a[contains(text(),'Register')]"
    login_button = By.XPATH, "//a[contains(text(),'Login')]"
    order_history_button = By.XPATH, "//a[contains(text(),'Order History')]"
    shopping_cart_button = By.XPATH, "//span[contains(text(),'Shopping Cart')]"
    currency_dropdown = By.ID, 'form-currency'
    currency_option = By.XPATH, "//a[contains(text(),'{}')]"
    currency_list = By.XPATH, "//ul[@class='dropdown-menu show']/child::li"
    cameras_tab = By.XPATH, "//a[text()='Cameras']"
    smartphones_tab = By.XPATH, "//a[contains(text(),'Phones')]"
    opencart_img = By.XPATH, "//img[@title='Your Store']"
    logout_button = By.XPATH, "//a[contains(text(),'Logout')]"
    components_dropdown = By.XPATH, "//a[contains(text(),'Components')]"
    monitors_option = By.XPATH, "//a[contains(text(),'Monitors')]"
    wishlist_button = By.XPATH, "//span[contains(text(),'Wish List')]"
    cart_button = By.ID, "cart"
    checkout_cart_button = By.XPATH, "//strong[contains(text(),'Checkout')]"
    my_account_dropdown = By.XPATH, "//a[@title='My Account']"
    my_account_button = By.XPATH, "//a[contains(text(),'My Account')]"
    search_field = By.XPATH, "//input[@name='search']"
    search_button = By.XPATH, "//i[@class='fa fa-search']"
