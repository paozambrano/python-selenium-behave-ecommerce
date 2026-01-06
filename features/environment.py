from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

print("\n>>> ENVIRONMENT.PY FILE LOADED SUCCESSFULLY<<<")

def before_scenario(context, scenario):
    print(">>> EXECUTING BEFORE_scenario: Starting Driver...")
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    print(">>> EXECUTING AFTER_scenario: Closing Driver...")
    if hasattr(context, 'driver'):
        context.driver.quit()
