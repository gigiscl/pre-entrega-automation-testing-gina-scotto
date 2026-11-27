import requests
import pytest_check as check
from utils.logger import logger

# Prueba de GET
def test_obtener_usuario(base_url,headers):
    logger.info("Iniciando prueba para obtener usuario de la API.")
    # URL a la que se accedera para obtener recursos segun la documentacion de la API
    url = f"{base_url}/users/2"

    # Se almacena la información de la solicitud en la variable response
    response = requests.get(url,headers=headers)

    # NIVEL 1: STATUS CODE
    logger.info("Iniciando validaciones de status code")
    codigo = response.status_code
    assert codigo == 200
    logger.info("Se realizo exitosamente la operación, se obtuvo el codigo 200.")

    # NIVEL 2: HEADERS
    logger.info("Iniciando validaciones de headers")
    # Verificación de que el formato recibido del servidor es en formato json
    assert "application/json" in response.headers["Content-Type"]
    logger.info("Se verificó que el formato de la informaçión es de tipo json")

    # NIVEL 3: ESTRUCTURA
    logger.info("Iniciando validaciones de estructura.")
    # información que se almacena del servidor
    data = response.json()

    # Validar que el contenido sea un diccionario
    assert isinstance(data,dict) 
    logger.info("Se verificó que el elemento recibido en data es un diccionario.")
    assert "data" in data
    logger.info("Se verificó que dentro del diccionario hay una clave 'data'")
    assert isinstance(data["data"],dict)
    logger.info("Se verificó que dentro de data hay otro diccionario")

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]
    logger.info("Se verificó que dentro de data hay id, email, first_name y last_name")

    # NIVEL 4: CONTENIDO
    logger.info("Iniciando validaciones de contenido.")
    assert data["data"]["id"] == 2
    logger.info("Se verificó el valor del id es igual a 2")
    assert data["data"]["email"] == "janet.weaver@reqres.in"
    logger.info("Se verificó que el valor del email es igual a janet.weaver@regres.in")

    # NIVEL 5: TIEMPO DE RESPUESTA
    logger.info("Iniciando validaciones de tiempo de respuesta.")
    assert response.elapsed.total_seconds() < 2
    logger.info("Se verificó que el tiempo total en segundos desde el envio de la solicitud fue menor a 2s.")

# Prueba de POST
def test_crear_usuario(base_url,headers):
    logger.info("Iniciando prueba de creacion de usuario.")
    url = f"{base_url}/users/"

    # Variable con la información de usuario que se desea crear
    usuario = {
        "email":"gigi@bue.edu.ar",
        "first_name":"Gi",
        "last_name":"Scott",
        "job":"Tester"
    }

    # Se almacena la información de la solicitud en la variable response
    response = requests.post(url,headers=headers,json=usuario)

    # NIVEL 1 STATUS CODE
    logger.info("Iniciando validaciones de status code")
    assert response.status_code == 201
    logger.info("Se valido el status code es 201")

    # NIVEL 2 HEADERS
    logger.info("Iniciando validaciones de headers")
    assert "application/json" in response.headers["Content-Type"]
    logger.info("Se verificó que el formato de la información recibida es un json")

    # NIVEL 3 ESTRUCTURA
    logger.info("Iniciando validaciones de estructura.")
    data = response.json()
    # Validaciones suvaes cpn check en vez de assert para evitar la interrupcion total de la prueba
    check.is_in("email",data)
    check.is_in("first_name",data)
    check.is_in("last_name",data) 
    check.is_in("id",data)
    logger.info("Se verificó que en data se encuentran email, frist_name, last_name y id.")

    # NIVEL 4 CONTENIDO
    logger.info("Iniciando validaciones de contenido.")
    # Validaciones suvaes cpn check en vez de assert para evitar la interrupcion total de la prueba
    check.equal(data["email"],usuario["email"]) 
    check.equal(data["first_name"],usuario["first_name"]) 
    logger.info("Se verificó que el email y first_name creados son iguales a los envidados.")

    # NIVEL 5: TIEMPO DE RESPUESTA
    logger.info("Iniciando validaciones de tiempo de respuesta.")
    assert response.elapsed.total_seconds() < 2
    logger.info("Se verifico que demoro menos de 2 segundo en hacer la solicitud al servidor.")

# Prueba de DELETE
def test_eliminar_usuario(base_url,headers):
    logger.info("Iniciando prueba de eliminación de usuario.")
    url = f"{base_url}/users/2"

    # Se almacena la información recibida en response
    response = requests.delete(url,headers=headers)
    
    # NIVEL 1: STATUS CODE
    logger.info("Iniciando validación de status code.")
    assert response.status_code == 204
    logger.info("Se verificó que el estatus code es igual a 204.")
    
    # NIVEL 2: HEADERS
    logger.info("Iniciando validación de headers")
    assert "Content-Type" not in response.headers
    logger.info("Se verificó que no hay un json.")
    
    # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
    logger.info("Iniciando validaciones de estructura y contenido.")
    assert len(response.content) == 0
    logger.info("Se verifico que el contenido esta vacio.")
    
    # NIVEL 5: TIEMPO DE RESPUESTA
    logger.info("Iniciando validaciones de tiempo de respuesta")
    assert response.elapsed.total_seconds() < 2
    logger.info("Se verificó que la solicitud duró menos de 2 segundos.")
    
{
    "data":{
        "id":2,
        "email":"gigi@bue.edu.ar",
        "nombre":"Gi",
        "apellido":"Scott"
    },
    "support":{}
}