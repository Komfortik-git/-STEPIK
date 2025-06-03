from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')  # уточнили локатор
    PRICE_ELEMENT = (By.CSS_SELECTOR, ".product_main > p.price_color")
    EXPECTED_SUCCESS_TEXT = "Coders at Work был добавлен в вашу корзину."

#messages > div:nth-child(1) > div
#div.alertinner > strong
    def add_to_basket(self):
        add_button = self.find_element(*ProductPage.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def wait_for_success_message(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )  # ждём появления сообщения

    def check_success_message(self):
        try:
            # Ожидаем появления элемента с сообщением
            success_message = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
            ).text.strip()

            # Проверяем точное совпадение текста
            if success_message == self.EXPECTED_SUCCESS_TEXT:
                return True
            else:
                return False

        except TimeoutException:
            return False# учитываем русскую и английскую локализацию
