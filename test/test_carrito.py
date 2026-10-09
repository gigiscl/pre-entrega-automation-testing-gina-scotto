from selenium.webdriver.common.by import By

# Modulos necesarios para agregar esperas con excepciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

def test_carrito(driver_logueado):
    #Se genera el logueo llamando a la funcion del test_login
    driver = driver_logueado

     # Espera explicita
    espera = WebDriverWait(driver, 10)
 
    # Espera a que el primer producto sea visible
    primer_producto = espera.until(e.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

    # Asignar a una variable el nombre del primer producto de la web
    nomb_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Acceder al boton de agregar al carrito
    boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
    boton_agregar.click()

    # Se agrega una nueva espera a que el producto sea visible como añadidio al carrito
    contador_carrito = espera.until(e.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    # Validacion de que el producto se agrego al carrito
    assert contador_carrito.text == "1"

    # Verificar que el boton del carrito sea clickeable y cuando sea clickeable, hacerle click
    espera.until(e.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_badge"))).click()

    # Verificar que el elemento esta en el carrito

    producto_carrito = espera.until(e.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    assert nomb_producto == producto_carrito
