from behave import when, then
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@when('I add the first product to the cart')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_first_product()

@when('I click "{button_name}"')
def step_impl(context, button_name):
    if button_name == "Continue Shopping":
        context.product_page.continue_shopping()
    elif button_name == "View Cart":
        context.product_page.view_cart()

@when('I add the second product to the cart')
def step_impl(context):
    context.product_page.add_second_product()

@then('I verify both products are in the cart')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    items = context.cart_page.get_all_cart_data()
    assert len(items) == 2, f"Expected 2 items, but found {len(items)}"

@then('I verify prices, quantities, and total prices')
def step_impl(context):
    items = context.cart_page.get_all_cart_data()
    for item in items:
        assert item["price"] != ""
        assert item["quantity"] == "1"
        assert item["total"] != ""
        print(f"Verified product: {item['name']}")
