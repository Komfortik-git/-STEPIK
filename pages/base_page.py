from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url=url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator_type, selector):
        return self.browser.find_element(locator_type, selector)

    def click_on_element(self, locator_type, selector):
        element = self.find_element(locator_type, selector)
        element.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = float(alert.text.split()[2])
        answer = str(math.log(abs((12 * math.sin(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return alert_text
        except NoAlertPresentException:
            return None

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorized user"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception:
            return False
        return True
