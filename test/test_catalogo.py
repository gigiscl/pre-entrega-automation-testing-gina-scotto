from selenium.webdriver.common.by import By
from pages.catalogo_page import CatalogoPage
from utils.logger import logger


def test_catalogo(driver_logueado):
    try:
        logger.info("Iniciando la prueba del catalogo.")
        catalogo_page = CatalogoPage(driver_logueado)
    
        logger.info("Ingreso al inventory.")
        # Se accede a los productos del catalogo
        productos = catalogo_page.lista_productos()
        logger.info("Captura de todos los productos disponibles.")
        
        # Comprueba que hay elementos en el inventory
        logger.info("Verificando si hay productos.")
        assert len(productos) > 0
        logger.info("Se verifico que hay al menos un producto.")
    
        # Validaciones de que coincida con los datos de la web
        logger.info("Prueba de integridad de nombre y precio de un producto.")
        assert catalogo_page.nombre_primer_producto() == "Sauce Labs Backpack"
        logger.info("Se verificó que es correcto el nombre del producto")
        assert catalogo_page.precio_primer_producto() == "$29.99"
        logger.info("Se verificó que es correcto el precio del producto.")

        # Elementos de la interfaz precenstes
        assert catalogo_page.existe_menu() # Se verifica que este visible
        logger.info("Se encuentra visible el menú desplegable")
        assert catalogo_page.existe_filtro()
        logger.info("Se encuentra disponible el filtro para los productos.")

    except Exception:
        logger.exception("Hubo un error en la prueba del inventario.")
        raise





