from pages.base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        input_email.send_keys(email)
        input_pass1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION_INPUT)
        input_pass1.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION_INPUT)
        input_pass2.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_register.click()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "/login/" in current_url, "Current URL does not contain '/login/'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"
