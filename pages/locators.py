# pages/locators.py

from selenium.webdriver.common.by import By

class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    TOTAL_COST = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-total strong")
class LoginPageLocators:
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTRATION_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    SUCCESS_REGISTER_MESSAGE = (By.CSS_SELECTOR, ".alertinner.wicon")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".basket-total strong")
