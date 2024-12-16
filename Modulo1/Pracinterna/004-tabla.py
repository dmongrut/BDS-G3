tabla = int(input("Ingresa la tabla a multiplicar: "))

for contador in range(1,13,1):
  resultado = tabla * contador
  print(f"El numero {tabla} x {contador} es {resultado}")

print("Se termino de multiplicar toda la Tabla")