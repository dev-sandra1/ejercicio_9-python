#Problema de la mochila (Knapsack)
#El "problema de la mochila" es un clásico de optimización. Supón que tienes una mochila con una 
# capacidad máxima y una lista de objetos con pesos y valores. Escribe un programa que determine el máximo valor que se
#  puede obtener en la mochila sin exceder su capacidad. Usa programación dinámica para resolverlo
#Si los objetos son [(peso=1, valor=10), (peso=3, valor=20), (peso=4, valor=30)] y 
# la capacidad es 5, el máximo valor posible es 40 (los objetos de peso 1 y peso 4).

def knapsack(capacidad, pesos, valores, n):
    dp = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacidad + 1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], valores[i-1] + dp[i-1][w-pesos[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacidad]

pesos = [1, 3, 4]
valores = [10, 20, 30]
capacidad = int(input("Introduce la capacidad de la mochila: "))
n = len(pesos)
max_valor = knapsack(capacidad, pesos, valores, n)
print(f"El valor máximo que se puede obtener es: {max_valor}")
