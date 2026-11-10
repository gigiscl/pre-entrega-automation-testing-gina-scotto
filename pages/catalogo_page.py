from selenium.webdriver.common.by import By

class CatalogoPage:
    def __init__(self, driver):
        self.driver = driver

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

