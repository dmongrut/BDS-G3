import os
from time import sleep

#PROGRAMA PARA CONVERTIR MONEDAS DE SOLES A DOLARES Y DE DOLARES A SOLES

#ENTRADA
TIPO_CAMBIO_COMPRA = 3.7
TIPO_CAMBIO_VENTA = 3.8

bandera =  True

#PROCESO
while (bandera):
  print("""
        ===============================================
          [1] CONVERTIR SOLES A DOLARES
          [2] CONVERTIR DOLARES A SOLES
          [3] SALIR        
        ===============================================
        """)
  
  opcion = int(input("Elija una opcion: "))
  os.system("clear")

  if (opcion == 1):
    print("""
          ===============================================
                  CONVIRTIENDO SOLES A DOLARES
          ===============================================
          """)
    monto_origen = float(input("Ingrese monto en soles: "))
    monto_destino = monto_origen / TIPO_CAMBIO_VENTA
    print(f"EL MONTO EN DOLARES ES {monto_destino}")

  elif (opcion == 2):
      print("""
            ===============================================
                    CONVIRTIENDO DOLARES A SOLES
            ===============================================
            """)
      monto_origen = float(input("Ingrese monto en dolares: "))
      monto_destino = monto_origen * TIPO_CAMBIO_COMPRA
      print(f"EL MONTO EN DOLARES ES {monto_destino}")

  elif (opcion == 3):
      bandera = False
      print("SALIENDO DEL PROGRAMA")

  else:
      print("La opcion no es valida!!!")
      break
      
  sleep(2)
  os.system("clear")

#SALIDA