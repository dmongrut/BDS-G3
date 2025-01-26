capitales = {
  "Peru":"Lima",
  "Ecuador":"Quito",
  "Chile":"Santiago",
  "Colombia":"Bogota"
}


# Recorrido por claves
print("="*50 + "RECORRIDO POR CLAVES")
for clave in capitales.keys():
  print(clave)
  
print("="*50)

# Recorrido por valores
print("="*50 + "RECORRIDO POR VALORES")
for valor in capitales.values():
  print(valor)

# Recorrido por clave, valor
print("="*50 + "RECORRIDO POR CLAVE,VALOR")
for clave,valor in capitales.items():
  print(f"La capital de {clave} es {valor}")