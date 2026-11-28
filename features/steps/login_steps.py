from behave import given,when,then
from pages.login_page import LoginPage

@given("el usuario debes estar en la pagina del login")
def step_usuario_en_login(context):
    context.login_page = LoginPage(context.driver)

@when('ingresa en los campos de datos "{usuario}" y "{contraseña}"')
def step_ingresar_credenciales(context,usuario,contraseña):
    if usuario == "VACIO":
        usuario = ""

    if contraseña == "VACIO":
        contraseña = ""

    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_contraseña(contraseña)

@when("hace click en el boton de login")
def step_click_login(context):
    context.login_page.click_login()

@then("deberia ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url

@then('deberia mostrase el mensaje de error "{mensaje}" y permanecer en la pagina de login')
def step_validar_mensaje_error(context,mensaje):
    error = context.login_page.mensaje_error()
    print(error)
    assert mensaje in error, f"Se esperaba '{mensaje}', pero se obtuvo '{error}'"
    


