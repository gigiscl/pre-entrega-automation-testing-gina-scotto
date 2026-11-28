from behave import given,when,then
from pages.login_page import LoginPage
from pages.catalogo_page import CatalogoPage


@given("el usuario inicia sesion exitosamente y se encuentra en el catalogo")
def step_usuario_en_catalogo(context):
    context.catalogo_page = CatalogoPage(context.driver)
    login_page = LoginPage(context.driver)
    login_page.login()

@when('se accede a la lista de todos los productos disponibles en el catalogo')
def step_obtener_lista_productos(context):
    context.productos = context.catalogo_page.lista_productos()

@then("deberia haber al menos un producto en el inventory")
def step_validar_hay_productos(context):
     assert len(context.productos) > 0

@then('el primer producto deberia llamarse "{nombre}" con un precio de "{precio}"')
def step_validar_nombre_precio_del_producto(context, nombre, precio):
    assert context.catalogo_page.nombre_primer_producto() == nombre
    assert context.catalogo_page.precio_primer_producto() == precio

@then("deberia estar visible el menú desplegable")
def step_validar_menu_visible(context):
    assert context.catalogo_page.existe_menu()

@then("deberia estar visible el filtro de productos")
def step_validar_filtro_visible(context):
    assert context.catalogo_page.existe_filtro()




