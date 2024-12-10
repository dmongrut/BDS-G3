import os
from time import sleep

#PROGRAMA PARA CONVERTIR MONEDAS DE SOLES A DOLARES Y DE DOLARES A SOLES

#ENTRADA
TIPO_CAMBIO_COMPRA = 3.7
TIPO_CAMBIO_VENTA = 3.8

bandera = True

#PROCESO
while (bandera):
  os.system("clear")
  print("""
        ======================================================
                    CONVERTIDOR DE MONEDAS
        ======================================================
          [1] CONVERTIR DE SOLES A DOLARES (VENTA)
          [2] CONVERTIR DE DOLARES A SOLES (COMPRA)
          [3] SALIR
        ======================================================
                """)
  
  opcion = int(input("Elija una opcion: "))
  os.system("clear") 

  if(opcion == 1):
      print("""
            ======================================================
                      CONVIRTIENDO SOLES A DOLARES
            ======================================================
            """)
      monto_origen = float(input("Ingrese el monto en soles: "))
      monto_destino = monto_origen / TIPO_CAMBIO_VENTA
      print(f"EL MONTO EN DOLARES ES {monto_destino}")
   
  elif(opcion == 2):
      print("""
                ======================================================
                          CONVIRTIENDO DOLARES A SOLES
                ======================================================
            """)
 
      monto_origen = float(input("Ingrese el monto en dolares: "))
      monto_destino = monto_origen * TIPO_CAMBIO_COMPRA
      print(f"EL MONTO EN SOLES ES {monto_destino}")
   
  elif(opcion == 3):
      bandera = False
      print("SALIENDO DEL PROGRAMA")
    
  else:
      print("La opcion no es valida")
      break
  
  sleep(2)
  os.system("clear")

#SALIDA

