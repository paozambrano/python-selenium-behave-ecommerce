from behave import when, then
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

@when('I click "View Product" of the first product')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.click(context.product_page.VIEW_PRODUCT_FIRST)

@when('I fill the review form with name "{name}", email "{email}" and comment "{comment}"')
def step_impl(context, name, email, comment):
    context.product_page.fill_review(name, email, comment)

@when('I click "Submit Review"')
def step_impl(context):
    context.product_page.submit_review()