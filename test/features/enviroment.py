from selenium import webdriver

def before_scenario(context,scenario):
    context.driver = webdriver.Edge()

def after_scenario(context,scenario):
    context.driver.quit()

