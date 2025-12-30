from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    PRODUCTS_NAV_BUTTON = (By.CSS_SELECTOR, 'a[href="/products"]')
    SEARCH_INPUT = (By.ID, "search_product" )
    SEARCH_BUTTON = (By.ID, "submit_search")
    ALL_PRODUCTS_TITLE = (By.CSS_SELECTOR, ".features_items h2.title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "single-products")

    def go_to_products(self):
        self.click(self.PRODUCTS_NAV_BUTTON)

    def search_for_product(self, product_name):
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_results_title(self):
        return self.get_text(self.ALL_PRODUCTS_TITLE)
    
    def is_product_visible(self):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return len(products) > 0 