import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name", default="chrome")  # Устанавливаем Chrome по умолчанию
    if not browser_name.strip():  # Если имя браузера пустое или состоит из пробелов
        browser_name = "chrome"  # Принудительное присвоение Chrome
    browser = None
    if browser_name.lower() == "chrome":  # Приводим имя браузера к нижнему регистру для надежности сравнения
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"--browser_name should be chrome or firefox, but got '{browser_name}'")
    yield browser
    print("\nquit browser..")
    browser.quit()

    import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser after test.")
    browser.quit()
