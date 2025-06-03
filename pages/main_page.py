from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    """Класс, представляющий главную страницу интернет-магазина."""

    def go_to_login_page(self):
        """Метод для перехода на страницу авторизации."""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Проверяет наличие ссылки на вход на странице."""
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Ссылка на вход не найдена."

# Сам тестовый кейс
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
