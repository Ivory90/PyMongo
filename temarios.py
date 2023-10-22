from pymongo import MongoClient
from menu import generar_menu
from bson.objectid import ObjectId


def nuevo_manual():
    print('¿Quiere indentificar una ID numérica?')
    respuesta = input('si/no:')
    if respuesta == 'si':
        manual = {
            "_id": int(input('Id:')),
            "titulo": input('Titulo:'),
            "autor": input('Autor:'),
            "colaboradores": [],
            "paginas": int(input('Páginas:')),
            "finalizado": int(input('Finalizado (0/1):'))
        }
    else:
        manual = {
            "titulo": input('Titulo:'),
            "autor": input('Autor:'),
            "colaboradores": [],
            "paginas": int(input('Páginas:')),
            "finalizado": int(input('Finalizado (0/1):'))
        }         
    result = manuales.insert_one(manual)
    print(f"Manual insertado: {result.inserted_id}")


def modificar_manual():
    atributos = ['titulo', 'autor', 'paginas', 'finalizado']
    print('¿Quiere modificar un manual con ID numérico?')
    respuesta = input('si/no:')

    if respuesta == 'si':
        id = int(input('Id:'))
    else:
        id = ObjectId(input('Id:')) 

    print(f"Elija uno de estos atributos: {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}")
    atr = input('Atributo:')
    while atr not in atributos:
        print(f"Tiene que elegir uno de estos atributos: {atributos[0]}, {atributos[1]}, {atributos[2]}, {atributos[3]}")
        generar_menu
        atr = input('Atributo:')
    if atr == 'paginas':
        nuevo_valor = int(input('Nuevo valor:'))
        result = manuales.update_one({'_id':id},{'$set':{atr:nuevo_valor}})
    elif atr == 'finalizado':
        nuevo_valor = int(input('Nuevo valor:'))
        result = manuales.update_one({'_id':id},{'$set':{atr:nuevo_valor}})
    else:
        nuevo_valor = input('Nuevo valor:')
        result = manuales.update_one({'_id':id},{'$set':{atr:nuevo_valor}})
    print(f"Manual modificado: {result.modified_count}")

             
def insert_colaborador():
    print('¿Quiere modificar un manual con ID numérico?')
    respuesta = input('si/no:')

    if respuesta == 'si':
        id = int(input('Id:'))
    else:
        id = ObjectId(input('Id:'))

    nuevo_valor = input('Nuevo colaborador:')
    result = manuales.update_one({'_id':id},{'$push':{'colaboradores':nuevo_valor}})
    print(f"Manual modificado: {result.modified_count}")       


def eliminar_manual():
    print('¿Quiere eliminar un manual con ID numérico?')
    respuesta = input('si/no:')

    if respuesta == 'si':
        id = int(input('Id:'))
    else:
        id = ObjectId(input('Id:'))
        
    result = manuales.delete_one({'_id':id})
    print(f"Manual eliminado: {result.deleted_count}")       


def lista_manuales():
    for manual in manuales.find():
            print("=================")
            print("Id: ", manual["_id"])
            print("Titulo: ", manual["titulo"])
            print("Autor: ", manual["autor"])
            print("colaboradores: ",manual["colaboradores"])
            print("Paginas: ", manual["paginas"])
            print("Finalizado",manual["finalizado"])
            #print(manual)


def manuales_x_autor():
    aut = input('Autor:')
    for manual in manuales.find({'autor':aut}):
            print("=================")
            print("Id: ", manual["_id"])
            print("Titulo: ", manual["titulo"])
            print("Autor: ", manual["autor"])
            print("colaboradores: ",manual["colaboradores"])
            print("Paginas: ", manual["paginas"])
            print("Finalizado",manual["finalizado"]) 
            #print(manual)


def manuales_x_paginas():
    min = int(input('Mín. Págs.:'))
    max = int(input('Máx. Págs.:'))
    for manual in manuales.find({'$and':[{'paginas': {'$gt':min} } , {'paginas':{ '$lt':max} }]}):
            print("=================")
            print("Id: ", manual["_id"])
            print("Titulo: ", manual["titulo"])
            print("Autor: ", manual["autor"])
            print("Colaboradores: ",manual["colaboradores"])
            print("Paginas: ", manual["paginas"])
            print("Finalizado",manual["finalizado"]) 
            #print(manual)    


def opcion_salida():
    print('Adiós') 

     
if __name__ == '__main__':

    # Conexión
    client = MongoClient()

    # Abrir bd
    db = client.temarios

    # Especificar colección
    manuales = db.manuales

    opciones = {
        '1': (' Nuevo manual', nuevo_manual),
        '2': (' Modificar manual', modificar_manual),
        '3': (' Insertar colaborador', insert_colaborador),
        '4': (' Eliminar manual', eliminar_manual),
        '5': (' Ver todos los manuales', lista_manuales),
        '6': (' Lista de manuales por autor', manuales_x_autor),
        '7': (' Manuales por número de páginas', manuales_x_paginas),
        '8': (' Salir', opcion_salida)        
    }
    
    generar_menu(opciones, '8')

    client.close()



