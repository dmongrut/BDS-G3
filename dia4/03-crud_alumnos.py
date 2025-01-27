import os
from time import sleep
from matriculas.lib_alumnos import *

"""
CRUD
  - CREATE
  - READ
  - UPDATE
  - DELETE
"""
opcion = 0
while(opcion < 5):
  os.system("clear")
  menu()
  opcion = int(input("INGRESE OPCION : "))
  os.system("clear")
  
  if opcion == 1:
    dic_nuevo_alumno = registrar() 
    dic_alumnos.update(dic_nuevo_alumno)
  elif opcion == 2:
    mostrar(dic_alumnos)
    input("Presione ENTER para continuar...")
  elif opcion == 3:
    actualizar(dic_alumnos)    
  elif opcion == 4:
    eliminar(dic_alumnos)    
  elif opcion == 5:
    mostrar_mensaje("[5] SALIR")
  else:
    mostrar_mensaje("OPCION INVALIDA!!!")
  sleep(1)