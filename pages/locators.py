from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#id_login-username")
    REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FORM_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    SUCCESS_MESAGE = (By.CSS_SELECTOR, '#messages>div:nth-child(1) strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner p strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.XPATH, "//*[@id='content_inner']")
    ITEM_MESSAGE = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2")

