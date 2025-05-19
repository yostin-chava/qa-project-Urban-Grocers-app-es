import sender_stand_request
import data

#########################################################################
## Funcion asertiva positiva, se compara el que el codigo de respuesta ##
## sea 201 y que el name del kit sea el mismo al de la solititud       ##
#########################################################################
def positive_assert(kit_body):
    # Modificamos el body con la datos de prueba
    body = sender_stand_request.modify_body_kit(kit_body)

    # Enviamos la solicitud para crear la kit
    response_create_kit = sender_stand_request.post_new_client_kit(body)
    # El servidor deberia responder con 201
    assert response_create_kit.status_code == 201
    # verificamos que el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
    assert response_create_kit.json()["name"] == body["name"]

    #Obtenemos el name (nombre del kit) de la respuesta al crear el kit
    name1 = response_create_kit.json()["name"]
    #Verificamos que el kit creado si este en la base de datos con el endpoint GET "Recibir una kit por el nombre"
    response_verify_kit = sender_stand_request.get_verify_create_kit(name1)
    # La respuesta debe ser 200, lo que confirma que el kit si esta en la base de datos
    assert response_verify_kit.status_code == 200

##################################################
## Funcion asertiva negativa, se compara que el ##
## codigo de respuesta sea 400                  ##
##################################################
def negative_assert_code_400(kit_body):
    # Modificamos el body con la datos de prueba
    body = sender_stand_request.modify_body_kit(kit_body)

    # Enviamos la solicitud para crear la kit
    response_create_kit = sender_stand_request.post_new_client_kit(body)
    # El servidor deberia responder con error 400
    assert response_create_kit.status_code == 400

######################################################
## Prueba 1: El número permitido de caracteres (1): ##
## Se pasa el parametro kit_body = {"name": "a"}    ##
######################################################
def test_1_create_kit_with_one_character_name():
    positive_assert({"name": "a"})

###############################################################
## Prueba 2: El número permitido de caracteres (511):        ##
## Se pasa el parametro kit_body que esta en el archivo data ##
###############################################################
def test_2_create_kit_with_511_characters_name():
    positive_assert(data.kit_body_test_2)

###############################################################################
## Prueba 3: El número de caracteres es menor que la cantidad permitida (0): ##
## Se pasa el parametro kit_body = {"name": ""}                              ##
###############################################################################
def test_3_create_kit_with_empty_name_should_return_400():
    negative_assert_code_400({"name": ""})

#################################################################################
## Prueba 4: El número de caracteres es mayor que la cantidad permitida (512): ##
## Se pasa el parametro kit_body que esta en el archivo data                   ##
#################################################################################
def test_4_create_kit_with_511_characters_name_should_return_400():
    negative_assert_code_400(data.kit_body_test_4)

########################################################
## Prueba 5: Se permiten caracteres especiales:       ##
## Se pasa el parametro kit_body = {"name": ""№%@","} ##
########################################################
def test_5_create_kit_with_special_character_name():
    positive_assert({"name":"\"№%@\","})

#######################################################
## Prueba 6: Se permiten espacios:                   ##
## Se pasa el parametro kit_body = {"name": "A Aaa"} ##
#######################################################
def test_6_create_kit_with_space_in_name():
    positive_assert({"name": "A Aaa"})

#####################################################
## Prueba 7: Se permiten números:                  ##
## Se pasa el parametro kit_body = {"name": "123"} ##
#####################################################
def test_7_create_kit_with_number_string_name():
    positive_assert({"name": "123"})

########################################################
## Prueba 8: El parámetro no se pasa en la solicitud: ##
## Se pasa el parametro kit_body = { }                ##
########################################################
def test_8_create_kit_without_body_name_should_return_400():
    # Copiamos el body que tenemos en el archivo data
    body_modified = data.body_create_kit
    # Eliminamos la key "name" del body
    body_modified.pop("name")

    # Enviamos la solicitud para crear la kit
    response = sender_stand_request.post_new_client_kit(body_modified)
    # El servidor deberia responder con error 400
    assert response.status_code == 400

#####################################################################
## Prueba 8: Se ha pasado un tipo de parámetro diferente (número): ##
## Se pasa el parametro kit_body = {"name": 123}                   ##
#####################################################################
def test_9_create_kit_with_number_in_name_should_return_400():
    negative_assert_code_400({"name": 123})
