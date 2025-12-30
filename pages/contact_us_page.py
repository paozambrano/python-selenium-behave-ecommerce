from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, 'a[href="/contact_us"]')
    GET_IN_TOUCH_HEADER = (By.CSS_SELECTOR, ".contact-form h2.title")
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    SUBJECT_INPUT = (By.NAME, "subject")
    MESSAGE_INPUT = (By.ID, "message")
    UPLOAD_FILE_INPUT = (By.NAME, "upload_file")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".status.alert.alert-success")
    HOME_NAV_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")

    def go_to_contact_us(self):
        self.click(self.CONTACT_US_BUTTON)

    def fill_form(self, name, email, subject, message):
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.SUBJECT_INPUT, subject)
        self.type(self.MESSAGE_INPUT, message)

    def upload_file(self, file_path):
        self.find(self.UPLOAD_FILE_INPUT).send_keys(file_path)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)