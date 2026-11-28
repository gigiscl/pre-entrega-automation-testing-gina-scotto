Feature: Carrito de compras

    Scenario: Agregar producto al carrito
        Given el usuario inicia sesion exitosamente y se encuentra en el catalogo
        When se agrega "Sauce Labs Backpack" al carrito
        Then deberia haber "1" producto en el carrito
        And deberia verse el producto "Sauce Labs Backpack" con precio "29.99" al ingresar al carrito