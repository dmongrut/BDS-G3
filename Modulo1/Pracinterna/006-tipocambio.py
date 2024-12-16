#Tipo de Cambio - Que Apoya al Cambista de Dolares

tipo_cambio_compra = 3.7
tipo_cambio_venta = 3.8

importe = int(input("Ingrese el importe: "))
tipo_cambio = "si"
operacion = input ("Ingrese el tipo de operacion a realizar, (compra|venta): ")

while (tipo_cambio == "si"):
  if (operacion == "compra"):
    resultado = importe / 3.7
    print(f"Por {importe} soles son {resultado} dolares")

  elif (operacion == "venta"):
    resultado = importe * 3.8
    print(f"Por {importe} dolares son {resultado} soles")

  else:
    print(f"Operacion no existe!!!")
    exit()

  tipo_cambio = "no"