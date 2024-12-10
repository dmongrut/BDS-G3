tipo_cambio_compra = 3.7
tipo_cambio_venta = 3.8

importe = int(input("Ingrese el importe: "))
tipo_cambio = "si"
operacion = input ("ingrese el tipo de operacion a realizar, (compra | venta): ")

while (tipo_cambio == "si"):
        if (operacion == "compra"):
          resultado = importe / 3.7
          print(f"Por {importe} soles son {resultado} dolares")

        elif (operacion == "venta"):
          resultado = importe * 3.8
          print(f"Por {importe} dolares son {resultado} soles")
        
        else:
          print("Operacion no existe")
          exit()
        
        tipo_cambio = "no"

        """continuar = input("Desea continuar en el convertidor? (si/no): ")
        if (continuar == "si"):
           print("Que bueno")
           exit()
        else:
          print("Que malo")
           exit()"""