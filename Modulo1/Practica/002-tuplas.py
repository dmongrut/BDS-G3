dias = ("lunes","martes","miercoles","jueves")
print(dias)
print(type(dias))

#Para agregar datos convertimos la tupla en lista
print("=" * 20)
dias = list(dias)
print(type(dias))
dias.append("viernes")
print(dias)

print("=" * 20)
dias = tuple(dias)
print(type(dias))

#Recorrer una tupla(es igual a recorrer una lista)
print("=" * 20)
for dia in dias:
  print(dia)

