dias=["lunes","martes","miercoles"]
print(dias)

#Impresion a traves de indices
print(dias[0])
print(dias[1])
print(dias[2])
print("=" * 20)
print(dias[-1])
print(dias[-2])
print(dias[-3])

#Agregar valores a la lista
print("=" * 20)
dias.append("jueves")
dias.append("viernes")
print(dias)

#Eiminar un valor de la lista
print("=" * 20)
dias.pop(3)
print(dias)

print("=" * 20)
del dias[2:4]
print(dias)

dias.append("miercoles")
dias.append("jueves")
print(dias)

#Actualizar un valor
dias[2] = ("miercoles")
print(dias)

dias.append("viernes")
print(dias)

print("=" * 20)
nro_dias = len(dias)
print("El numero de dias es: ", nro_dias)

#Recorrer una lista
print("=" * 20)
for contador in range(len(dias)):
  print(dias[contador])