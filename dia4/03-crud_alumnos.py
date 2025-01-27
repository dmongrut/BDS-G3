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
dic_alumnos = {
  "12345678":{
    "nombre":"David",
    "email":"davidmongrut@gmail.com"
  }
}

ANCHO = 50
opcion = 0

while(opcion < 5):
  os.system("clear")
  menu(ANCHO)
  opcion = int(input("INGRESE OPCION : "))
  os.system("clear")
  
  if opcion == 1:
    dic_nuevo_alumno = registrar(ANCHO) 
    dic_alumnos.update(dic_nuevo_alumno)
  elif opcion == 2:
    mostrar(ANCHO, dic_alumnos)
    input("Presione ENTER para continuar...")
  elif opcion == 3:
    print("=" * ANCHO)
    print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
    print("*" * ANCHO)
    dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR")
    if dni in dic_alumnos:
      print(f"ALUMNO A ACTUALIZAR {dic_alumnos[dni]['nombre']}")
      nuevo_nombre = input("NOMBRE : ")
      nuevo_dni = input("DNI : ")
      nuevo_email = input("EMAIL : ")
      dic_act_alumno = {
        dni : {
            "nombre" : nuevo_nombre,
            "email"  : nuevo_email
        }
      }
      dic_alumnos.update(dic_act_alumno)
      print("ALUMNO ACTUALIZADO CON EXITO")
  elif opcion == 4:
    print("=" * ANCHO)
    print(" " * 10 + "[4] ELIMINAR ALUMNO")
    print("*" * ANCHO)
    dni = input("INGRESE EL DNI DEL ALUMNO A ELIMINAR : ")
    if dni in dic_alumnos:
      dic_alumnos.pop(dni)
      print("ALUMNO ELIMINADO")
  elif opcion == 5:
    print("=" * ANCHO)
    print(" " * 10 + "[5] SALIR")
    print("*" * ANCHO)    
  else:
    print("=" * ANCHO)
    print(" " * 10 + "OPCION INVALIDA!!!")
    print("*" * ANCHO)
  
  sleep(1)