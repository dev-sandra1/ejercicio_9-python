#Encontrar el número más frecuente en una lista

from collections import Counter

def numero_mas_frecuente(lista):
    contador = Counter(lista)
    # Obtener el número con la mayor frecuencia
    numero, _ = contador.most_common(1)[0]
    return numero

lista = list(map(int, input("Introduce una lista de números separados por espacio: ").split()))
resultado = numero_mas_frecuente(lista)
print(f"Número más frecuente: {resultado}")
