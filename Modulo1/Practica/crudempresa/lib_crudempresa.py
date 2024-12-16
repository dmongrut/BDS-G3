import os
from time import sleep

# Definir las variables del CRUD:
ancho_titulo = 50

# Definir el diccionario, coloque unos ejemplos previos de empresa
dic_empresas = {
    '10101010101':{
        'razon_social':'XYZ SAC',
        'direccion':'Lima'
        },
    '20202020202':{
        'razon_social':'ABC SAC',
        'direccion':'Surco'
        },
    '30303030303':{
        'razon_social':'MNO SAC',
        'direccion':'San Borja'
        }
}

def grabar_empresa(file_name):
    str_empresas = ""
    for empresa_clave,empresa_valor in dic_empresas.items():
        str_empresas += empresa_clave
        for registro_clave,registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'direccion':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(file_name,'w')
    fsalida.write(str_empresas)
    fsalida.close()



def mostrar_mensaje(texto):
    print("*" * ancho_titulo + "*" * ancho_titulo)
    if texto != " ":
        print(" " * 10 + texto)
        print("*" * ancho_titulo + "*" * ancho_titulo)
    

def menu():
    mostrar_mensaje("GESTION DE LA EMPRESA")
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    mostrar_mensaje(" ")

def registrar():
    mostrar_mensaje("[1] REGISTRAR EMPRESA")
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

def mostrar():
   mostrar_mensaje("[2] MOSTRAR EMPRESA")
   for ruc,datos in dic_empresas.items():
        print(f"RUC : {ruc}")
        print(f"Razon Social : {datos['razon_social']}")
        print(f"Dirección : {datos['direccion']}")
        print("*" * ancho_titulo)
        mostrar_mensaje(" ")

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
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

def eliminar():
    mostrar_mensaje("[3] ACTUALIZAR EMPRESA")
    ruc = input("INGRESE EL RUC DE LA EMPRESA QUE DESEA ELIMINAR: ")
    if ruc in dic_empresas:
        dic_empresas.pop(ruc)
        print("LA EMPRESA FUE ELIMINADA!!!")
        sleep(1)
    else:
        print("NO SE ENCONTRO EL RUC SOLICITADO!!!")
        sleep(1)

