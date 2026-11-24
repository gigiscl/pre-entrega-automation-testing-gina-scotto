import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest_html
import pathlib
import base64

from pages.login_page import LoginPage

@pytest.fixture
def driver_logueado(driver):
    login_page = LoginPage(driver)
    login_page.login()
    return driver

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

# funcion que será llamada para hacer las capturas 
# item = almacena información de la prueba.
# call = información de la ejecucion de etapas de la pruebas.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Se captura el driver con yield para almacenarlo.
    outcome = yield
    report = outcome.get_result()

    #Si se encuentra en el call y la prueba fallo
    if report.when == "call" and report.failed:
        # Se almacena en una variable toda la información de pruebas que usen el navegador.
        driver = item.funcargs.get("driver")

        # Se crea la carpeta donde se van a guardar las capturas de pantalla.
        carpeta = pathlib.Path("reports/sreenshots")
        carpeta.mkdir(parents=True,exist_ok=True) # si existe no crea la carpeta

        # Se genera el nombre y formato del archivo
        archivo = carpeta / f"{item.name}.png"

        # Realización de captura de pantalla
        driver.save_sreenshot(str(archivo))

        # Se perapara la imagen para incluirla al report, covirtiendo los datos
        # Se incrusta en el html en base64
        imagen = base64.b64encode(archivo.read_bytes()).decode("utf-8")

        # Se agrega a la imagen al report como una columna
        report.extras = [
            pytest_html.extras.png(imagen, name="Screenshot")
        ]