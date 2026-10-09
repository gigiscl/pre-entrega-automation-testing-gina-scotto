import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver_logueado():
    # Genera la variable driver que contiene el navegador
    driver = webdriver.Edge()

    # Tiempo de espera implicito no debe superar en cada acción
    driver.implicitly_wait(7)

    # Se ingresa a la url de la pagina que se realizaran los test
    driver.get("https://www.saucedemo.com/")

    # Se ingresan los datos username y pasword dentro de la pagina
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Con yield se puede pasar el logueo a otro test
    yield driver 
    
    # Cuando el test que lo utilice termine cerrara el navegador
    driver.quit()