from selenium import webdriver

def before_scenario(context,scenario):
    context.driver = webdriver.Edge()
    context.driver.implicitly_wait(7)
    context.driver.get("https://www.saucedemo.com/")

def after_scenario(context,scenario):
    context.driver.quit()

