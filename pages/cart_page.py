from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, "table tbody tr")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".cart_description h4 a")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".cart_price p")
    PRODUCT_QUANTITIES = (By.CSS_SELECTOR, ".cart_quantity button")
    PRODUCT_TOTALS = (By.CSS_SELECTOR, ".cart_total_price")

    PROCEED_CHECKOUT_BTN = (By.CSS_SELECTOR, ".check_out")
    REGISTER_LOGIN_LINK = (By.XPATH, "//u[text()='Register / Login']")
    COMMENT_AREA = (By.NAME, "message")
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, 'a[href="/payment"]')

    def get_all_cart_data(self):
        rows = self.driver.find_elements(*self.CART_ITEMS)
        cart_data = []
        for i in range(len(rows)):
            item = {
                "name": self.driver.find_elements(*self.PRODUCT_NAMES)[i].text,
                "price": self.driver.find_elements(*self.PRODUCT_PRICES)[i].text,
                "quantity": self.driver.find_elements(*self.PRODUCT_QUANTITIES)[i].text,
                "total": self.driver.find_elements(*self.PRODUCT_TOTALS)[i].text
            }
            cart_data.append(item)
        return cart_data