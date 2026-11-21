from selenium.webdriver.common.by import By

# Modulos necesarios ara agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

class CatalogoPage:
    def __init__(self, driver):
        self.driver = driver
        self.espera = WebDriverWait(driver, 10)

    def lista_productos(self):
        # Se traen todos los productos de la pagina que tengan la clase "inventory_item" y los retorna
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item")

    def nombre_primer_producto(self):
        nombre_prod = self.lista_productos()
 
        # Se accede al primer producto y se retorna su nombre
        return nombre_prod[0].find_element(By.CLASS_NAME, "inventory_item_name").text

    def precio_primer_producto(self):
        precio_prod = self.lista_productos()
        return precio_prod[0].find_element(By.CLASS_NAME, "inventory_item_price").text

    def existe_menu(self):
        menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
        return menu.is_displayed()
    
    def existe_filtro(self):
        filtro = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        return filtro.is_displayed()

    def agregar_producto_carrito(self, nombre):
        productos = self.lista_productos()

        # Recorrido de busqueda con el objetivo de encontrar el producto en la lista.
        for producto in productos:
            nombre_producto = producto.find_element(By.CLASS_NAME,"inventory_item_name").text
            if nombre_producto == nombre:
                print(nombre_producto)
                producto.find_element(By.TAG_NAME,"button").click()
                return

         # Usamos raise para lanzar un error en caso de que el nombre del producto no este.    
        raise AssertionError(f"No se encontró el producto: {nombre}")

    def cantidad_productos_carrito(self):
        return self.espera.until(e.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge"))).text

    def ir_al_carrito(self):
        self.espera.until(e.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()