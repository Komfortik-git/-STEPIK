import re
import pytest
from pages.product_page import ProductPage

@pytest.mark.parametrize('url_promo', ["newYear"])
def test_guest_can_add_product_to_basket(browser, url_promo):
    link = f" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207{url_promo}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    quiz_result = page.solve_quiz_and_get_code()

    # Парсим текст и получаем число
    match = re.search(r"Вставьте это число в поле ответа на Stepik: (\d+\.\d+)", quiz_result)
    if match:
        number = match.group(1)
        print(f"Your code: {number}")  # Печать номера для вставки в Stepik
        assert number is not None, "Не найдено число в результатах"
    else:
        assert False, f"Не удалось распарсить результат: {quiz_result}"
