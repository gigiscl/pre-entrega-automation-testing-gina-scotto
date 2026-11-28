from behave import given,when,then

from pages.catalogo_page import CatalogoPage
from pages.carrito_page import CarritoPage

@when('se agrega "{producto}" al carrito')
def step_agrega_producto_al_carrito(context, producto):
    context.catalogo_page.agregar_producto_carrito(producto)


@then('deberia haber "{cantidad}" producto en el carrito')
def step_validar_contador_carrito(context, cantidad):
    assert context.catalogo_page.cantidad_productos_carrito() == cantidad

@then('deberia verse el producto "{nombre}" con precio "{precio}" al ingresar al carrito')
def step_validar_producto_en_carrito(context, nombre, precio):
    context.catalogo_page.ir_al_carrito()
    carrito_page = CarritoPage(context.driver)
    assert carrito_page.get_nombre_producto() == nombre
    assert carrito_page.get_precio_producto() == float(precio)