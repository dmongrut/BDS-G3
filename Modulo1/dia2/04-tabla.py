tabla = int(input("ingrese la tabla a multiplicar: "))

for contador in range (1,13,1):
  resultado = tabla * contador
  print(f"El numero {tabla} x {contador} es igual a {resultado}")

print("Termino la tabla de multiplicar")