from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    PRODUCTS_NAV_BUTTON = (By.CSS_SELECTOR, 'a[href="/products"]')
    SEARCH_INPUT = (By.ID, "search_product" )
    SEARCH_BUTTON = (By.ID, "submit_search")
    ALL_PRODUCTS_TITLE = (By.CSS_SELECTOR, ".features_items h2.title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "single-products")
    PRODUCT_LIST = (By.CLASS_NAME, "features_items")

    VIEW_PRODUCT_FIRST = (By.XPATH, '(//a[text()="View Product"])[1]')

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_CATEGORY = (By.XPATH, "//p[contains(text(), 'Category')]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    PRODUCT_AVAILABILITY = (By.XPATH, "//b[text()='Availability:']/..")
    PRODUCT_CONDITION = (By.XPATH, "//b[text()='Condition:']/..")
    PRODUCT_BRAND = (By.XPATH, "//b[text()='Brand:']/..")

    FIRST_PRODUCT = (By.CSS_SELECTOR, ".single-products")
    FIRST_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, ".overlay-content a[data-product-id='1']")
    SECOND_PRODUCT_ADD_TO_CART = (By.CSS_SELECTOR, ".overlay-content a[data-product-id='2']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn-success.close-modal")
    VIEW_CART_LINK = (By.XPATH, "//u[text()='View Cart']")
    CART_LINK = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')

    def go_to_products(self):
        self.click(self.PRODUCTS_NAV_BUTTON)

    def click_first_product(self):
        self.click(self.VIEW_PRODUCT_FIRST)

    def search_for_product(self, product_name):
        self.type(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_results_title(self):
        return self.get_text(self.ALL_PRODUCTS_TITLE)
    
    def is_product_visible(self):
        products = self.driver.find_elements(*self.PRODUCT_ITEMS)
        return len(products) > 0 
    
    def get_product_details(self):
        return{
            "name": self.get_text(self.PRODUCT_NAME),
            "category": self.get_text(self.PRODUCT_CATEGORY),
            "price": self.get_text(self.PRODUCT_PRICE),
            "availability": self.get_text(self.PRODUCT_AVAILABILITY),
            "condition": self.get_text(self.PRODUCT_CONDITION),
            "brand": self.get_text(self.PRODUCT_BRAND)
        }
    
    def add_first_product(self):

        FIRST_PRODUCT_CARD = (By.XPATH, "(//div[@class='single-products'])[1]")
        element = self.find(FIRST_PRODUCT_CARD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        self.hover_over(self.FIRST_PRODUCT)
        
        OVERLAY_ADD_BTN = (By.XPATH, "(//a[@data-product-id='1'])[2]")
        self.click(OVERLAY_ADD_BTN)

    def add_second_product(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-content")))

        SECOND_PRODUCT_CARD = (By.XPATH, "(//div[@class='single-products'])[2]")
        self.hover_over(SECOND_PRODUCT_CARD)
        self.click(self.SECOND_PRODUCT_ADD_TO_CART)

    def continue_shopping(self):
        self.click(self.CONTINUE_BUTTON)

    def view_cart(self):
        self.click(self.VIEW_CART_LINK)
    
    def go_to_cart(self):
        self.click(self.CART_LINK)