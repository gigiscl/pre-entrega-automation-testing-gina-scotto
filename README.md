# Automation Testing con Selenium

Proyecto de QA Automation con Selenium para la pagina web **Sauce Demo** con el objetivo de realizar pruebas automatizadas dentro de la página. Se realizan pruebas de login, carrito, y otras pruebas de navegación, para el curso de Talento Tech.

## Tecnologias

- Python
- Pytest (con reporte-html)
- Selenium
- Git
- Github

## Instalación

*instalación de dependencias:*

python
``` pip install pytest
```

python
```pip install pytest-html
```

python
```pip install selenium
```

## Ejecución de pruebas

### Para ejecutar todos los test:

python
```pytest
```
Al terminar de ejecutarse los test, podrás visualizar los resultados abriendo el archivo reporte.html que se genera en la carpeta reports/.

### Para ejecutar un test en particular:

python
```pytest [test_nombre].py
```

## Casos de prueba
- Login exitoso: Se valida un login con las credenciales correctas para poder ingresar.
- Agregar producto al carrito: Se verifica que es posible agregar productos del inventory al carrito.
- Verificar producto en el carrito: Prueba que valida que un producto está en el carrito.






