from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

def test_login_exitoso(driver):
    # Se abre el navegador en la pagina
    login_page = LoginPage(driver)
    
    try:
        # Inicia sesion en la pagina 
        login_page.login("standard_user", "secret_sauce")

        #  Se genera una nueva variable que obtiene el titulo de la pagina
        titulo = driver.find_element(By.CLASS_NAME, "app_logo")

        # Asserts que prueban si se cumplen las condiciones esperadas
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert titulo.text == "Swag Labs"
    finally:
        driver.quit()


