# CRUD DE UNA EMPRESA: QUE CONTIENE RUC, RAZON SOCIAL Y DIRECCION, CON FUNCIONES Y QUE GRABA ARCHIVO

# Importar las librerías
import os
from time import sleep
from crudempresa.lib_crudempresa import *

# Definir las variables del CRUD:
opcion = 0

#Definir el menu
while (opcion < 5):
    os.system('clear')
    menu()
    opcion = int(input("INGRESE UNA OPCION : "))
    os.system("clear")

    if opcion == 1:
       registrar()

    elif opcion == 2:
       mostrar()
       input("Presion ENTER para continuar...")
        

    elif opcion == 3:
       actualizar()
       sleep(1)

    elif opcion == 4:
       eliminar()

    elif opcion == 5:
       grabar_empresa("empresacrud.txt")
       mostrar_mensaje("[5] SALIENDO!!!")
       sleep(1)
               
    else:
       mostrar_mensaje("OPCIÓN INVÁLIDA!!!")
       sleep(1)

    sleep(1)