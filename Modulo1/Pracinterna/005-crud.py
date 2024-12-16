import os
from time import sleep

"""
CRUD
  -CREATE
  -READ
  -UPDATE
  -DELETE
"""

#DICCIONARIO QUE REUNE TODA LA INFO: Con la clave del diccionario que es el DNI y 
# con el Valor que es segundo diccionario que contiene el Nombre y el Email
dic_alumnos = {
  "12345678" :{
    "nombre" : "Cesar",
    "email"  : "cesar.gmail.com"
               },
  "20202020" :{
    "nombre" : "Juan",
    "email" : "juan.gmail.com"
              },
  "30303030" :{
    "nombre" : "Pedro",
    "email" : "pedro.gmail.com"
              }
}

ANCHO = 50
opcion = 0

while(opcion <= 5):
  os.system("clear")
  print("=" * ANCHO)
  print(" " * 10 + "GESTION DE ALUMNOS")
  print("=" * ANCHO)
  print("""
        [1] REGISTRAR ALUMNO
        [2] MOSTRAR ALUMNOS
        [3] ACTUALIZAR ALUMNO
        [4] ELIMINAR ALUMNO
        [5] SALIR
        """)
  print("=" * ANCHO)
 
  opcion = int(input("INGRESE OPCION: "))
  os.system("clear")

  if opcion == 1:
      print("=" * ANCHO)
      print(" " * 10 + "[1] REGISTRAR ALUMNO")
      print("=" * ANCHO)
      dni = input("DNI    :")           #Captura el DNI y Sobreescribe (actualiza) si ya existe el DNI
      nombre = input("NOMBRE  :")
      email = input("EMAIL    :")
      dic_nuevo_alumno = {              #Crea el diccionario dic_nuevo_alumno con los datos capturados (DNI, Nombre y el Email)
          dni : {
                  "nombre":nombre,
                  "email": email
                }
      }
      dic_alumnos.update(dic_nuevo_alumno)   #Al diccionario dic_alumnos le hago update (actualizo o inserto) el diccionario dic_alumno_nuevo
                                             #que acabo de crear
    
  elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        for dni,datos in dic_alumnos.items():    #Recorro por la clave y el valor el diccionario dic_alumnos usando ... items()
            print(f"DNI : {dni}")                #Dentro del diccionario dic_alumnos: la clave{dni}
            print(f"Nombre : {datos['nombre']}") #Dentro del diccionario dic_alumnos, "sub diccionario dato": el valor de [nombre]
            print(f"EMAIL : {datos['email']}")   #Dentro del diccionario dic_alumnos, "sub diccionario dato": el valor del [email] 
            print("*" * ANCHO)
        input("Presion ENTER para continuar...")  #Espera hasta que se presiona una tecla, a fin de que pueda leer lo mostrado

  elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
        dni = input("INGRESE DNI DEL ALUMNO A ACTUALIZAR: ")
        if dni in dic_alumnos:                                         #Si el dni esta en el diccionario dic_alumnos
            #print(f"ALUMNO A ACTUALIZAR a {dni}")                     #DNI del alumno que ingrese
            #print(f"ALUMNO A ACTUALIZAR b {dic_alumnos}")             #DNI, Nombre y el Email de Todos
            #print(f"ALUMNO A ACTUALIZAR c {dic_alumnos,{dni}}")       #DNI, Nombre y el Email de Todos
            #print(f"ALUMNO A ACTUALIZAR d {dic_alumnos[dni]}")        #Nombre y el Email del alumno que ingrese
            print(f"ALUMNO A ACTUALIZAR e {dic_alumnos[dni]['nombre']}") #Muestra el nombre del alumno que voy a actualizar
            nuevo_nombre = input('NOMBRE : ')
            nuevo_dni = input('DNI  :')
            nuevo_email = input('EMAIL :')
            dic_act_alumno = {                  #Crea el diccionario dic_act_alumno con los datos capturados (Nombre y el Email)
                dni : {                         #Si deseamos que actualize el dni debe decir nuevo_dni (sino como aca queda con el dni anterior)
                    'nombre':nuevo_nombre,
                    'email':nuevo_email
                }
            }
            dic_alumnos.update(dic_act_alumno)  #Actualiza el diccionario dic_alumnos con el nuevo diccionario dic_act_alumno que acabo de crear
            print("ALUMNO ACTUALIZADO CON EXITO")

  elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("=" * ANCHO)
        dni = input("INGRESE EL DNI DEL ALUMNO A ELIMINAR : ")       #Solicito, capturo el dni que deseo eliminar
        if dni in dic_alumnos:                                       #Si el dni esta en el diccionario dic_alumnos
            dic_alumnos.pop(dni)                                     #Borra, elimina del diccionario dic_alumno el alumno con el dni ingresado
            print("ALUMNO ELIMINADO")
            sleep(1)
        else:
            print("NO SE ENCONTRO EL ALUMNO")

  elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "[5] SALIENDO")
        print("=" * ANCHO)
        sleep(1)
        #exit
        #pass
        break
  
  else:
        print("=" * ANCHO)
        print(" " * 10 + "OPCIÓN INVÁLIDA!!!")
        print("=" * ANCHO)
        sleep(1)
        #continue

  #sleep(1)