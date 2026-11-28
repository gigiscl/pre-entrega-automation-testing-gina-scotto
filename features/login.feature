Feature: Inicio de sesion
    Background:
        Given el usuario debes estar en la pagina del login

    Scenario: Inicio de sesion exitoso
        When ingresa en los campos de datos "standard_user" y "secret_sauce"
        And hace click en el boton de login
        Then deberia ingresar al inventario

    Scenario: Login invalido con contraseña incorrecta
        When ingresa en los campos de datos "standard_user" y "12345"
        And hace click en el boton de login
        Then deberia mostrase el mensaje de error "Epic sadface" y permanecer en la pagina de login
    Scenario Outline: Login invalido con diferentes credenciales
        When ingresa en los campos de datos "<usuario>" y "<password>"
        And hace click en el boton de login
        Then deberia mostrase el mensaje de error "<mensaje>"

        Examples:
            |usuario|password|mensaje|
            |standard_user|12354|Epic sadface: Username and password do not match any user in this service|
            |standart_user|secret_sauce|Epic sadface: Username and password do not match any user in this service|
            |VACIO|secret_sauce|Epic sadface: Username is required|
            |standard_user|VACIO|Epic sadface: Password is required|
    