from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

print("\n>>> ARCHIVO ENVIRONMENT.PY CARGADO CORRECTAMENTE <<<")

def before_scenario(context, scenario):
    print(">>> EJECUTANDO BEFORE_scenario: Iniciando Driver...")
    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def after_scenario(context, scenario):
    print(">>> EJECUTANDO AFTER_scenario: Cerrando Driver...")
    if hasattr(context, 'driver'):
        context.driver.quit()
