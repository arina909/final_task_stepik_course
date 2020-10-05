from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTER2 = (By.CSS_SELECTOR, "#id_registration-password2")
