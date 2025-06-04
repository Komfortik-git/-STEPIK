import re
import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage



# Тест для гостевого пользователя
@pytest.mark.parametrize('url_promo', ["newYear"])
def test_guest_can_add_product_to_basket(browser, url_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={url_promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    quiz_result = page.solve_quiz_and_get_code()

    # Парсим текст и получаем число
    match = re.search(r"Вставьте это число в поле ответа на Stepik: (\d+\.\d+)", quiz_result)
    if match:
        number = match.group(1)
        print(f"Your code: {number}")
        assert number is not None, "Не найдено число в результатах"
    else:
        assert False, f"Не удалось распарсить результат: {quiz_result}"

# Класс для тестов с пользователями
class TestUserAddToBasketFromProductPage:
    def test_user_can_add_product_to_basket(self, browser):
        # Регистрируем пользователя
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "strong_password123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

        # Переходим на страницу товара и добавляем его в корзину
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.add_to_basket()
        product_page.should_be_message_contains_book_name()
        product_page.should_be_message_with_total_cost()

    def test_user_cant_see_success_message(self, browser):
        # Регистрируем пользователя
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "strong_password123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

        # Переходим на страницу товара и проверяем отсутствие сообщения об успехе
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_not_be_success_message()
