Feature: Navegación en el Inventory

    Scenario: Inicio de sesion exitoso
        Given el usuario inicia sesion exitosamente y se encuentra en el catalogo
        When se accede a la lista de todos los productos disponibles en el catalogo
        Then deberia haber al menos un producto en el inventory
        And el primer producto deberia llamarse "Sauce Labs Backpack" con un precio de "$29.99"
        And deberia estar visible el menú desplegable
        And deberia estar visible el filtro de productos