#CRUD DE EMPRESA CON RUC, RAZON SOCIAL Y DIRECCION

# Importar librerías
import os
from time import sleep

# Definir los diccionarios:
dic_empresas = {
    '20608993399':{
        'razon_social':'DMYCM SOLUCIONES CORPORATIVAS SAC',
        'direccion':'Don Pompeyo 131, Surco'
    }
}

# Definicion de cada uno de los CRUD:
ancho_titulo = 50
opcion = 0

while (opcion < 5):
    os.system('clear')
    print("*"*ancho_titulo)
    print(" "*10 + "ADMINISTRACION DE LA EMPRESA")
    print("*"*ancho_titulo)
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
        print("*"*ancho_titulo)
        print(" "*10 + "REGISTRAR EMPRESA")
        print("*"*ancho_titulo)
        ruc = input("Ingrese el RUC de la empresa: ")
        razon_social = input("Ingrese la razón social: ")
        direccion = input("Ingrese la dirección: ")
        dic_nuevo_empresa = {
            ruc : {
                'razon_social': razon_social,
                'direccion': direccion
            }
        }
        dic_empresas.update(dic_nuevo_empresa)
    elif opcion == 2:
        print("*" * ancho_titulo)
        print(" " * 10 + "[2] MOSTRAR EMPRESA")
        print("*" * ancho_titulo)
        for ruc,datos in dic_empresas.items():
            print(f"RUC : {ruc}")
            print(f"Razon Social : {datos['razon_social']}")
            print(f"Dirección : {datos['direccion']}")
            print("*"*ancho_titulo)
    elif opcion == 3:
        print("*" * ancho_titulo)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("*" * ancho_titulo)
        print("Nota: Solo puede actualizar la razón social y la dirección")
        ruc = input("INGRESE EL RUC DE LA EMPRESA A ACTUALIZAR: ")
        if ruc in dic_empresas:
            print(f"EMPRESA A ACTUALIZAR {dic_empresas[ruc]['razon_social']}")
            nuevo_razsocial = input('Razón Social  : ')
            nuevo_direccion = input('Dirección  : ')
            dic_act_empresa = {
                ruc : {
                    'razon_social': nuevo_razsocial,
                    'direccion': nuevo_direccion
                }
            }
            dic_empresas.update(dic_act_empresa)
            print("LOS DATOS DE LA EMPRESA FUERON ACTUALIZADOS")
    elif opcion == 4:
        print("*" * ancho_titulo)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("*" * ancho_titulo)
        ruc = input("INGRESE EL RUC DE LA EMPRESA A ELIMINAR: ")
        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("LA EMPRESA FUE ELIMINADA")
        else:
            print("NO SE ENCONTRO EL RUC ESPECIFICADO")
    elif opcion == 5:
        print("*" * ancho_titulo)
        print(" " * 10 + "[5] SALIR")
        print("*" * ancho_titulo)
    else:
        print("*" * ancho_titulo)
        print(" " * 10 + "OPCIÓN NO VALIDA!!!")
        print("*" * ancho_titulo)

    sleep(1)