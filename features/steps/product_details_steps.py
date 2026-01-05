from behave import then, when
from pages.product_page import ProductPage

@given('I verify that home page is visible')
def step_impl(context):
    assert "Automation Exercise" in context.driver.title

@when('I navigate to the products page')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.go_to_products()

@then ('I verify user is navigated to "{expected_title}" page successfully')
def step_impl(context, expected_title):
    actual_title = context.product_page.get_results_title()
    assert expected_title.upper() in actual_title.upper()

@then ('the products list is visible')
def step_impl(context):
    assert context.product_page.find(context.product_page.PRODUCT_LIST).is_displayed()

@when('I click on "View Product" of the first product')
def step_impl(context):
    context.product_page.click_first_product()

@then('I am landed to the product detail page')
def step_impl(context):
    assert "product_details" in context.driver.current_url

@then('I verify that details are visible: name, category, price, availability, condition, brand')
def step_impl(context):
    details = context.product_page.get_product_details()

    assert details["name"] != "", "Product name is missing"
    assert "Category" in details["category"], "Category is missing"
    assert "Rs." in details["price"], "Price is missing or incorrect format"
    assert "Availability" in details["availability"], "Availability info is missing"
    assert "Condition" in details["condition"], "Condition info is missing"
    assert "Brand" in details["brand"], "Brand info is missing"