from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "e-mail for login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Password for login is not presented"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTER), "e-mail for register is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER1), "Password for register is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_REGISTER2), "Confirm password for register is not presented"
