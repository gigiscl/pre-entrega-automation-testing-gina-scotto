from selenium.webdriver.common.by import By
from pages.catalogo_page import CatalogoPage
from pages.carrito_page import CarritoPage
from utils.reader import lector_productos_json
from utils.logger import logger

def test_carrito(driver_logueado):
    try:
        logger.info("Iniciando prueba de carrito.")
        catalogo_page = CatalogoPage(driver_logueado)
        carrito_page = CarritoPage(driver_logueado)

        # Asignar a una variable el nombre del primer producto del json
        producto = lector_productos_json()[0]
        logger.info("Capturando primer producto del json.")
        print(producto)

        # Se agrega el producto seleccionado al carrito mediante el nombre
        catalogo_page.agregar_producto_carrito(producto["nombre"])
        logger.info("Se agregó el primer producto del json al carrito.")
        
        # Validacion de que el producto se agrego al carrito
        assert catalogo_page.cantidad_productos_carrito() == "1"
        logger.info("Se verificó la prieba del contador del carrito.")

        catalogo_page.ir_al_carrito()
        logger.info("Se redirigio a la pagina del carrito")

        # Verificar que el elemento esta en el carrito
        logger.info("Se inician pruebas de integridad de los datos.")
        assert carrito_page.get_nombre_producto() == producto["nombre"]
        logger.info("Se valido el nombre del producto en el carrito es igual al del json")
        assert carrito_page.get_precio_producto() == producto["precio"]
        logger.info("Se validó el precio del producto en el carrito es igual al del json.")
    except Exception:
        logger.info("Hubo un error en la prueba del carrito.")
        raise
