# CRUD DE UNA EMPRESA: RUC, RAZON SOCIAL Y DIRECCION

# Importar las librerías
import os
from time import sleep

# Definir el diccionario:
dic_empresas = {
    '10101010101':{
        'razon_social':'XYZ SAC',
        'direccion':'Lima, Lima'
        },
    '20202020202':{
        'razon_social':'ABC SAC',
        'direccion':'Surco, Surco'
        },
    '30303030303':{
        'razon_social':'MNO SAC',
        'direccion':'San Borja, San Borja'
        }
}

# Definir las variables del CRUD:
ancho_titulo = 50
opcion = 0

#Definir el menu
while (opcion < 5):
    os.system('clear')
    print("*" * ancho_titulo)
    print(" " * 10 + "ADMINISTRACION DE LA EMPRESA")
    print("*" * ancho_titulo)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    
    print("*" * ancho_titulo)
    opcion = int(input("INGRESE UNA OPCION : "))
    os.system("clear")

    if opcion == 1:
        print("*" * ancho_titulo)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("*" * ancho_titulo)
        ruc = input("Ingrese el RUC de la empresa - 11 Digitos: ")
        razon_social = input("Ingrese la razón social de la empresa: ")
        direccion = input("Ingrese la dirección de la empresa: ")
        dic_nueva_empresa = {
            ruc : {
                'razon_social': razon_social,
                'direccion': direccion
            }
        }
        dic_empresas.update(dic_nueva_empresa)

    elif opcion == 2:
        print("*" * ancho_titulo)
        print(" " * 10 + "[2] MOSTRAR EMPRESA")
        print("*" * ancho_titulo)
        for ruc,datos in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon Social : {datos['razon_social']}")
            print(f"Dirección : {datos['direccion']}")
            print("*" * ancho_titulo)
        input("Presion ENTER para continuar...")

    elif opcion == 3:
        print("*" * ancho_titulo)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("*" * ancho_titulo)
        ruc = input("INGRESE EL RUC DE LA EMPRESA QUE DESEA ACTUALIZAR: ")
        if ruc in dic_empresas:
            print(f"EMPRESA A ACTUALIZAR {dic_empresas[ruc]['razon_social']}")
            nueva_razonsocial = input('Ingrese la Nueva Razón Social  : ')
            nueva_direccion = input('Ingrese la Nueva Dirección  : ')
            dic_act_empresa = {
                ruc : {
                    'razon_social': nueva_razonsocial,
                    'direccion': nueva_direccion
                }
            }
            dic_empresas.update(dic_act_empresa)
            print("LOS DATOS DE LA EMPRESA FUERON ACTUALIZADOS!!!")
            sleep(1)

    elif opcion == 4:
        print("*" * ancho_titulo)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("*" * ancho_titulo)
        ruc = input("INGRESE EL RUC DE LA EMPRESA QUE DESEA ELIMINAR: ")
        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("LA EMPRESA FUE ELIMINADA!!!")
            sleep(1)
        else:
            print("NO SE ENCONTRO EL RUC SOLICITADO!!!")
            sleep(1)

    elif opcion == 5:
        print("*" * ancho_titulo)
        print(" " * 10 + "[5] SALIENDO!!!")
        print("*" * ancho_titulo)
        sleep(1)
        #break
        
    else:
        print("*" * ancho_titulo)
        print(" " * 10 + "OPCIÓN NO VALIDA!!!")
        print("*" * ancho_titulo)
        sleep(1)

    sleep(1)