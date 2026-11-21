from selenium.webdriver.common.by import By

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

class CarritoPage:
    def __init__(self, driver):
        self.driver = driver
        self.espera = WebDriverWait(driver, 10)


    
    def get_nombre_producto(self):
        # Espera a que el primer producto sea visible
        return self.espera.until(e.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text

    def get_precio_producto(self):
        precio = self.espera.until(e.visibility_of_element_located((By.CLASS_NAME,"inventory_item_price"))).text

        # se le saca el signo de pesos al texto para poder compararlo con el texto del json
        return float(precio.replace("$",""))

    