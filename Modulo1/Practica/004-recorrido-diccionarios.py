import os
from time import sleep

os.system("clear")
sleep(0.5)

print("=================PAISES y CAPITALES===================")

capitales = {
          "Peru" : "Lima",
          "Ecuador" : "Quito",
          "Chile" : "Santiago",
          "Colombia"  : "Bogota"
}

#Recorrido por Claves
print(" " * 16 + "RECORRIDO POR CLAVES")
for clave in capitales.keys():
  print(clave)
sleep(2)
#os.system("clear")

#Recorrido por Valores
print(" " * 16 + "RECORRIDO POR VALORES")
for valor in capitales.values():
  print(valor)
sleep(2)

#Recorrido por Clave y Valor
print(" " * 13 + "RECORRIDO POR CLAVE Y VALOR")
for clave,valor in capitales.items():
  print(f"La capital de {clave} es {valor}")
sleep(2)
