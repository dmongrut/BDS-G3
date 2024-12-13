import os
from time import sleep
#importa del paquete matriculas (directorio) el modulo lib_alumnos el cual tiene dentro tiene funciones como cargar alumnos, etc.
from matriculas.lib_alumnos import *

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

#Esta dentro de lib_alumnos y le pasos como parametros alumnos.txt
cargar_alumnos('alumnos.txt')
opcion = 0

while(opcion < 5):
    os.system("clear")
    menu()
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        registrar()
    elif opcion == 2:
        mostrar()
        input("Presion ENTER para continuar...")
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        grabar_alumnos('alumnos.txt')
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("OPCIÓN INVÁLIDA!!!")
    sleep(1)