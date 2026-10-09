from selenium.webdriver.common.by import By

def test_catalogo(driver_logueado):
    #Se genera el logueo llamando a la funcion del test_login
    driver = driver_logueado

    # Se acede al los productos del catalogo
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    print(productos)
    print(f"Elementos_{len(productos)}")

    # Comprueba que hay elementos en el inventory
    assert len(productos) > 0

    # Guarda en una variable el primer producto de la lista
    primer_producto = productos[0]

    # Variables para obtener el nombre y el precio del primer producto
    nombre_product = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio_product = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    # Validaciones de que coincida con los datos de la web
    assert nombre_product == "Sauce Labs Backpack"
    assert precio_product == "$29.99"


    # Elementos de la interfaz precenstes

    menu_desplegable = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_desplegable.is_displayed() # Se verifica que este visible

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()





