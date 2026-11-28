from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.reader import lector_users_csv
from utils.logger import logger
import pytest

@pytest.mark.parametrize(
        "data", lector_users_csv())

 
def test_login_exitoso(driver, data):
    logger.info("Iniciando prueba del login.")
    login_page = LoginPage(driver)
    
    try:
        # Inicia sesion en la pagina 
        login_page.login(data["usuario"],data["contrasena"])
        logger.info("Ingreso de credenciales.")

        if(login_page.sigue_en_login()):
            error = login_page.mensaje_error()
            print(error)
            assert "Epic sadface" in error
            logger.info("Login invalido con captura de mensaje de error.")
        else:
            #  Se genera una nueva variable que obtiene el titulo de la pagina
            titulo = driver.find_element(By.CLASS_NAME, "app_logo")

            # Asserts que prueban si se cumplen las condiciones esperadas
            assert driver.current_url == "https://www.saucedemo.com/inventory.html"
            assert titulo.text == "Swag Labs"
            logger.info("Login exitoso.")
    except Exception:
        logger.exception("Hubo un error en la prueba del login.")
        raise


