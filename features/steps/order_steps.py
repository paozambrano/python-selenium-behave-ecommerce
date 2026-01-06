from behave import given, when, then
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I add the first product to the cart")
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_first_product()

@given('I click "View Cart"')
def step_impl(context):
    context.product_page.view_cart()

@then('I verify that cart page is displayed')
def step_impl(context):
    assert "view_cart" in context.driver.current_url

@when('I fill signup name "{name}" and email "{email}"')
def step_impl(context, name, email):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.signup_quick(name, email)

@when('I complete the full registration form')
def step_impl(context):
    context.driver.find_element(By.ID, "password").send_keys("Pass123")
    context.driver.find_element(By.ID, "first_name").send_keys("Pao")
    context.driver.find_element(By.ID, "last_name").send_keys("Test")
    context.driver.find_element(By.ID, "address1").send_keys("123 Street")
    context.driver.find_element(By.ID, "country").send_keys("United States")
    context.driver.find_element(By.ID, "state").send_keys("NY")
    context.driver.find_element(By.ID, "city").send_keys("NYC")
    context.driver.find_element(By.ID, "zipcode").send_keys("10001")
    context.driver.find_element(By.ID, "mobile_number").send_keys("123456")
    context.driver.find_element(By.CSS_SELECTOR, '[data-qa="create-account"]').click()

@then('I verify "{text}" is visible')
def step_impl(context, text):
    # 1. Espera pequeña para que la página se estabilice
    time.sleep(3) 
    
    # 2. Intentamos leer todo el texto de la página usando JavaScript (infalible)
    # Esto obtiene lo que el navegador realmente tiene renderizado
    page_text = context.driver.execute_script("return document.body.innerText")
    
    if text.lower() in page_text.lower():
        print(f"✅ Texto '{text}' encontrado mediante JS")
        return

    # 3. Si falla, refrescamos una vez (por si el anuncio bloqueó el renderizado)
    context.driver.refresh()
    time.sleep(3)
    
    final_text = context.driver.execute_script("return document.body.innerText")
    assert text.lower() in final_text.lower(), f"Error: No se encontró '{text}' incluso tras refresh y JS."

@then('I click "Continue" button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Continue").click()
    time.sleep(2)
    context.driver.refresh()

@then('I verify address details and review order')
def step_impl(context):
    assert context.driver.find_element(By.ID, "address_delivery").is_displayed()

@when('I enter comment "{comment}" and click "Place Order"')
def step_impl(context, comment):
    context.cart_page = CartPage(context.driver)
    context.driver.find_element(By.NAME, "message").send_keys(comment)
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/payment"]').click()

@when('I enter payment details "{name}", "{card}", "{cvc}", "{month}", "{year}"')
def step_impl(context, name, card, cvc, month, year):
    context.checkout_page.fill_payment(name, card, cvc, month, year)

@then('I verify success message "{message}"')
def step_impl(context, message):
    assert message in context.driver.page_source
