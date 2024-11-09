#Encuentra el primer número que falta en una secuencia

def primer_numero_faltante(lista):
    for i in range(len(lista) - 1):
        if lista[i + 1] != lista[i] + 1:
            return lista[i] + 1
    return lista[-1] + 1

lista = list(map(int, input("Introduce una lista de números consecutivos separados por espacio: ").split()))
resultado = primer_numero_faltante(sorted(lista))
print(f"El primer número faltante en la secuencia es: {resultado}")
