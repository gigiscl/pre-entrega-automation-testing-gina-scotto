from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.catalogo_page import CatalogoPage


def test_catalogo(driver):
    login_page = LoginPage(driver)
    catalogo_page = CatalogoPage(driver)

    # Inicio de sesion en la pagina
    login_page.login()

    # Se acede a los productos del catalogo
    productos = catalogo_page.lista_productos()
    
    print(productos)
    print(f"Elementos_{len(productos)}")

    # Comprueba que hay elementos en el inventory
    assert len(productos) > 0

    # Validaciones de que coincida con los datos de la web
    assert catalogo_page.nombre_primer_producto() == "Sauce Labs Backpack"
    assert catalogo_page.precio_primer_producto() == "$29.99"

    # Elementos de la interfaz precenstes
    assert catalogo_page.existe_menu() # Se verifica que este visible
    assert catalogo_page.existe_filtro()





