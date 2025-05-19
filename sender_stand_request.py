import data
import configuration
import requests

###################################
## Funcion para crear el usuario ##
###################################

def post_create_user():
    # Enviamos la solicitud post con la url, el endpoint, el header y el cuerpo de la solicitud
    return requests.post(configuration.url_api + configuration.api_create_user,
                         headers=data.header_create_user,
                         json=data.body_crate_user)

######################################################
## Funcion para obtener el token del usuario creado ##
## y formar el header para crear el kit del usuario ##
######################################################

def get_new_user_token():
    # Obtemos el token al crear el usuario
    auth_token = post_create_user().json()
    # Se hace una copia del header que esta en el archivo data
    new_header = data.header_create_kit.copy()
    # Formamos el nuevo header agregando el token que extraimos anteriormente
    new_header['Authorization'] = "Bearer " + auth_token['authToken']
    # Retornamos el nuevo header
    return new_header

###########################################################
## Funcion para obtener el body del kit para las pruebas ##
## Se modifica el nombre que va a tener el kit
###########################################################
def modify_body_kit(name):
    new_body = data.body_create_kit.copy()
    new_body['name'] = name["name"]
    return new_body

###########################################
## Funcion para crear el kit del usuario ##
###########################################
def post_new_client_kit(body):
    # Llamamos la funcion que no crea el header que enviamos para crear el kit de usuario
    header_kit = get_new_user_token()
    # Enviamos la solicitud post con la url, el endpoint, el header y el cuerpo de la solicitud
    return requests.post(configuration.url_api + configuration.api_create_kit,
                         headers=header_kit,
                         json=body)

######################################################################
## Funcion para verificar si el kit esta creado en la base de datos ##
######################################################################
def get_verify_create_kit(kit_name):
    # El nombre del kit lo pasamos a string en caso de que se hayan pasado numeros
    name = str(kit_name)
    # Si hay espacios en el nombre
    if " " in name:
        # si hay espacios remplazamos %20 en los espacios
        new_name = name.replace(" ", "%20")
    else:
        # Si no hay espacios el nombre queda igual
        new_name = name

    # Enviamos la solicitud get con la url, el endpoint y el nombre del kit
    return requests.get(configuration.url_api + configuration.api_verify_kit + new_name)