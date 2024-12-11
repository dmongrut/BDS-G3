capitales = {
          "Peru": "Lima",
          "Ecuador": "Quito",
          "Chile": "Santiago",
          "Colombia": "Bogota"
  }
'''print(capitales["Chile"])'''

pais = input("Ingrese el pais: ")
##capital = capitales[pais]

if pais in capitales:
  capital = capitales.get(pais)
  print(f"La capital de {pais} es {capital}")
  eliminar_capital = input("¿Desea eliminar la capital? (si, no)")
  if eliminar_capital == "si":
    capitale.pop(pais,"NO ESISTE")
    print(capitales)
else:
  print(f"No se encontro la capital del {pais}")
  nueva_capital = input(f"Ingrese la capital de {pais}: ")
  capitales.update({pias:nueva_capital})
  print(capitales)
