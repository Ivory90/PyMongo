# Funciones para crear un menu

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f'{clave}{opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input ('Opción: ')) not in opciones:
        print('Opción incorrecta, Escoja una de las siguientes opciones:')
        mostrar_menu(opciones)
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    mostrar_menu(opciones)
    while opcion != opcion_salida:
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)


