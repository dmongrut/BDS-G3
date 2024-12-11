import os
from time import sleep

sleep(2)
os.system("cls")

print("====PAISES===")

capitales = {
          "Peru": "Lima",
          "Ecuador": "Quito",
          "Chile": "Santiago",
          "Colombia": "Bogota"
  }

#Reccorido por claves
print(""*50 + "RECORRIDO POR CLAVES")
for clave in capitales.keys():
    print(clave)
sleep(2)

os.system("cls")
#Reccorido por valores
print(""*50 + "RECORRIDO POR VALORES")
for valor in capitales.values():
    print(valor)
sleep(2)

os.system("cls")
#Reccorido por clave, valor
print(""*50 + "RECORRIDO POR CLAVE Y VALOR")
for clave, valor in capitales.items():
    print(f"la capital de {clave} es {valor}")
