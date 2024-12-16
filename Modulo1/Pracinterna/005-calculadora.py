bandera = "si"

while (bandera == "si"):
  print("======================== CALCULADORA PYTHON ========================")
  numero1 = int(input("Numero 1: "))
  numero2 = int(input("Numero 2: "))
  operacion = int(input("""Ingrese el tipo de operacion
                        1) SUMA
                        2) RESTA
                        3) MULTIPLICACION
                        4) DIVISION
                        INGRESE UNA OPCION: """))
  
  if (operacion == 1):
    resultado = numero1 + numero2
    print(f"La suma de {numero1} + {numero2} es {resultado}")

  elif (operacion == 2):
    resultado = numero1 - numero2
    print(f"La resta de {numero1} - {numero2} es {resultado}")

  elif (operacion == 3):
    resultado = numero1 * numero2
    print(f"La multiplicacion de {numero1} x {numero2} es {resultado}")
  
  elif (operacion == 4):
    resultado = numero1 / numero2
    print(f"La división de {numero1} + {numero2} es {resultado}")

  else:
    print("Operacion no existe!!!")

  bandera = input ("¿Desea continuar? (si|no): ")