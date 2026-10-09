from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex


def test_login_exitoso():
    # Se asigna a una variable el navegador a usar
    driver = webdriver.Edge()

    # Tiempo de espera maximo para cada acciónss 
    driver.implicitly_wait(7)

    # Espera explicita
    espera = WebDriverWait(driver, 10)


    try:
        # Se ingresa a la web que se va a testear con su url
        driver.get("https://www.saucedemo.com/")

        # Creación de variables que contienen el elemento de la web mediante su ID
        usuario = driver.find_element(By.ID, "user-name")
        contrasenia = driver.find_element(By.ID, "password")

        # Se esperara a que sea clickeable el boton
        boton_login = espera.until(ex.element_to_be_clickable((By.ID, "login-button")))
        
        # interacción con la pagina usando las variables anteriores
        usuario.send_keys("standard_user")
        contrasenia.send_keys("secret_sauce")
        boton_login.click()

        #  Se genera una nueva variable que obtiene el titulo de la pagina
        titulo = driver.find_element(By.CLASS_NAME, "app_logo")

        # Asserts que prueban si se cumplen las condiciones esperadas
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert titulo.text == "Swag Labs"
    finally:
        driver.quit()


test_login_exitoso()
