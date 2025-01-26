bandera = "si"
while(bandera == "si"):
  print("===========CALCULADORA CON PYTHON===================")
  numero1 = int(input("Numero 1 : "))
  numero2 = int(input("Numero 2 : "))
  operacion = int(input(""" Ingrese el tipo de operacion
                      1) SUMA
                      2) RESTA
                      3) MULTIPLICACION
                      4) DIVISION
                  """))
  if(operacion == 1):
    resultado = numero1 + numero2
    print(f"La suma de {numero1} + {numero2} es {resultado}")
  elif(operacion == 2):
    resultado = numero1 - numero2
    print(f"La resta de {numero1} - {numero2} es {resultado}")
  elif(operacion == 3):
    resultado = numero1 - numero2
    print(f"La multiplicacion de {numero1} * {numero2} es {resultado}")
  elif(operacion == 4):
    resultado = numero1 - numero2
    print(f"La division de {numero1} / {numero2} es {resultado}")
  else:
    print("La operacion no existe")
        
  bandera = input("Desea continuar...?(si,no):")