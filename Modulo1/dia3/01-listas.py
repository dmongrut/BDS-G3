dias = ["lunes","martes","miercoles"]
print(dias)
#Impresion a traves de INDICES
print(dias[0])
print(dias[1])
print(dias[2])
print("=============")
print(dias[-1])
print(dias[-2])
print(dias[-3])

#Agregar valores a la lista
print("=============")
dias.append("jueves")
dias.append("viernes")
print(dias)

#Eliminar un valor de la lista
print("=============")
dias.pop(3)
print(dias)

print("=============")
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


print("===================")
nro_dias = len(dias)
print("El numero de dias es: ", nro_dias)

#Recorrer una lista
print("===================")
for contador in range (len(dias)):
  print(dias[contador])

 
print("===================")
for dia in dias:
    print(dia)
