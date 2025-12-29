from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'div.login-form input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'div.login-form input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div.login-form button[type="submit"]')
    LOGGED_IN_AS = (By.XPATH, '//*[@id="header"]//li[10]/a')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.login-form p[style*="color: red"]')

    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_user_status(self):
        return self.get_text(self.LOGGED_IN_AS)