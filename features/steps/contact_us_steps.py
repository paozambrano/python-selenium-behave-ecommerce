import os
from behave import given, when, then
from pages.contact_us_page import ContactUsPage

@then('I verify that home page is visible')
def step_impl(context):
    assert "Automation Exercise" in context.driver.title

@when('I click on "Contact Us" button')
def step_impl(context):
    context.contact_page = ContactUsPage(context.driver)
    context.contact_page.go_to_contact_us()

@then('I verify "GET IN TOUCH" is visible')
def step_impl(context):
    header = context.contact_page.get_text(context.contact_page.GET_IN_TOUCH_HEADER)
    assert "GET IN TOUCH" in header.upper()

@when('I enter name "{name}", email "{email}", subject "{subject}", and message "{message}"')
def step_impl(context, name, email, subject, message):
    context.contact_page.fill_form(name, email, subject, message)

@when('I upload a file')
def step_impl(context):
    file_path = os.path.abspath("test.txt")
    with open(file_path, "w") as f:
        f.write("Test file for automation")
    context.contact_page.upload_file(file_path)

@when('I click "Submit" button')
def step_impl(context):
    context.contact_page.submit_form()

@when('I accept the confirmation alert')
def step_impl(context):
    context.contact_page.handle_alert()

@then('I verify success message "{message}" is visible')
def step_impl(context, message):
    success_text = context.contact_page.get_text(context.contact_page.SUCCESS_MESSAGE)

@when('I click the "Home" button')
def step_impl(context):
    context.contact_page.click(context.contact_page.HOME_NAV_BUTTON)

@then('I verify that I landed to home page successfully')
def step_impl(context):
    assert context.driver.current_url == "https://automationexercise.com/"