from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.catalogo_page import CatalogoPage
from pages.carrito_page import CarritoPage
from utils.reader import lector_productos_json

def test_carrito(driver):
    login_page = LoginPage(driver)
    catalogo_page = CatalogoPage(driver)
    carrito_page = CarritoPage(driver)

    login_page.login()

    # Asignar a una variable el nombre del primer producto del json
    producto = lector_productos_json()[0]
    print(producto)

    # Se agrega el producto seleccionado al carrito mediante el nombre
    catalogo_page.agregar_producto_carrito(producto["nombre"])
    
    # Validacion de que el producto se agrego al carrito
    assert catalogo_page.cantidad_productos_carrito() == "1"

    catalogo_page.ir_al_carrito()

    # Verificar que el elemento esta en el carrito
    assert carrito_page.get_nombre_producto() == producto["nombre"]
    assert carrito_page.get_precio_producto() == producto["precio"]
