def sumar(n1, n2):
    resultado = n1 + n2 
    return resultado


def sumar_con_mensaje(n1, n2):
    resultado = int(n1) + int(n2)
    print(f"SUMA CON MENSAJE: la suma de {n1} + {n2} es {resultado}")


n1 = input("Ingrese numero1: ")
n2 = input("Ingrese numero2: ")

suma = sumar(int(n1), int(n2))
print(f"La suma de {n1} + {n2} es {suma}")

sumar_con_mensaje(n1,n2)

#print(sumar(50,70))