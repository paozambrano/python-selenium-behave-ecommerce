from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def visit(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self, locator):
        self.find(locator).click() 
    
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
    
    def handle_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def hover_over(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()