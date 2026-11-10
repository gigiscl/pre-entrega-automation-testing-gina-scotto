from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.reader import lector_users_csv
import pytest
import time

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex


@pytest.mark.parametrize(
        "data", lector_users_csv())


def test_login_exitoso(driver, data):
    # Se abre el navegador en la pagina
    login_page = LoginPage(driver)
    
    try:
        # Inicia sesion en la pagina 
        login_page.login(data["usuario"],data["contrasena"])

        if(login_page.sigue_en_login()):
            error = login_page.mensaje_errpr()
            print(error)
            assert "Epic sadface" in error
        else:
            #  Se genera una nueva variable que obtiene el titulo de la pagina
            titulo = driver.find_element(By.CLASS_NAME, "app_logo")

            # Asserts que prueban si se cumplen las condiciones esperadas
            assert driver.current_url == "https://www.saucedemo.com/inventory.html"
            assert titulo.text == "Swag Labs"

    finally:
        driver.quit()


