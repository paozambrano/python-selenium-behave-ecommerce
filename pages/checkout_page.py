from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    SIGNUP_NAME = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
    SIGNUP_EMAIL = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')
    SIGNUP_BTN = (By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button')
    REGISTER_LOGIN_LINK = (By.XPATH, '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a')
    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, ".check_out")

    NAME_ON_CARD = (By.NAME, "name_on_card")
    CARD_NUMBER = (By.NAME, "card_number")
    CVC = (By.NAME, "cvc")
    EXP_MONTH = (By.NAME, "expiry_month")
    EXP_YEAR = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.ID, "submit")

    SUCCESS_ORDEN_MSG = (By.CSS_SELECTOR, "#success_message .alert-success")
    DELETE_ACCOUNT_BTN = (By.CSS_SELECTOR, 'a[href="/delete_account"]')

    def proceed_checkout(self):
        self.click(self.PROCEED_CHECKOUT_BTN)

    def register_login(self):
        self.click(self.REGISTER_LOGIN_LINK)

    def signup_quick(self, name, email):
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BTN)

    def fill_payment(self, name, card, cvc, month, year):
        self.type(self.NAME_ON_CARD, name)
        self.type(self.CARD_NUMBER, card)
        self.type(self.CVC, cvc)
        self.type(self.EXP_MONTH, month)
        self.type(self.EXP_YEAR, year)
        self.click(self.PAY_BUTTON)

    def delete_account(self):
        self.click(self.DELETE_ACCOUNT_BTN)