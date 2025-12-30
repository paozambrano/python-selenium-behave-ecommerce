from behave import given, when, then
from pages.product_page import ProductPage

@given('I am on the home page')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.visit("https://automationexercise.com/")

@when('I navigate to the product page')
def step_impl(context):
    context.product_page.go_to_products()

@when('I search for "{product_name}"')
def step_impl(context, product_name):
    context.product_page.search_for_product(product_name)

@then('I should see "{expected_title}" as the title')
def step_impl(context, expected_title):
    actual_title = context.product_page.get_results_title()
    assert expected_title.upper() in actual_title.upper(), f"Expected {expected_title} but got {actual_title}"

@then('I should see results for the search')
def step_impl(context):
    assert context.product_page.is_product_visible(), "No products were found for the search criteria"