from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def add_to_basket(self):
        add_button = self.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def wait_for_success_message(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )

    def check_success_message(self):
        try:
        # Ждём появления сообщения
         success_message = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
         ).text.strip()

        # Частичная проверка текста сообщения
         return any(text in success_message for text in [
            "Coders at Work был добавлен в вашу корзину.",
            "Книга была добавлена в корзину.",  # учтем разные варианты локализации
            "Book has been added to your basket.",  # англоязычная версия
         ])
        except TimeoutException:
         return False

    def should_be_message_contains_book_name(self):
        actual_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        expected_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert expected_title in actual_message, f"Название книги '{expected_title}' не обнаружено в сообщении"

    def should_be_message_with_total_cost(self):
        try:
        # Ждём появления элемента с суммой корзины
          total_price_element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_TOTAL_PRICE)
        )
          total_price = total_price_element.text.strip()
        # Здесь можно добавить дополнительную проверку суммы корзины
          return bool(total_price)  # возвращаем True, если текст не пустой
        except TimeoutException:
          return False
    def should_not_be_success_message(self):
       try:
        # Ждём появления элемента с суммой корзины
          total_price_element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.BASKET_TOTAL_PRICE)
        )
          total_price = total_price_element.text.strip()
        # Здесь можно добавить дополнительную проверку суммы корзины
          return bool(total_price)  # возвращаем True, если текст не пустой
       except TimeoutException:
          return False
