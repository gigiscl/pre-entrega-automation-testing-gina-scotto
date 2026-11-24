import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Genera la variable driver que contiene el navegador
    driver = webdriver.Edge()

    # Tiempo de espera implicito no debe superar en cada acción
    driver.implicitly_wait(7)

    # Se ingresa a la url de la pagina que se realizaran los test
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    api_key = input("Ingresa tu x-api-key: ")
    return { "x-api-key": api_key}

