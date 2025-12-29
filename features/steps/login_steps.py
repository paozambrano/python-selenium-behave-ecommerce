from behave import given, when, then
from pages.login_page import LoginPage

@given('I navigate to the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.visit("https://automationexercise.com/login")

@when('I enter email "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.login_page.login(email, password)

@then('I should see "Logged in as" on the navbar')
def step_impl(context):
    status_text = context.login_page.get_user_status()
    assert "Logged in as" in status_text

@then('I should see an error message')
def step_impl(context):
    error_text = context.login_page.get_text(context.login_page.ERROR_MESSAGE)
    assert "your email or password is incorrect" in error_text.lower()