# Christian Torres Aguayo

import random

# Creamos una lista vacía para almacenar los números aleatorios
numeros_random = []

# Generamos 30 números aleatorios y los agregamos a la lista
for _ in range(1, 31):
    numero = random.randint(1, 300)  # Genera un número aleatorio entre 1 y 300
    numeros_random.append(numero)

# Imprimimos la lista de números aleatorios
print("Lista de números aleatorios:")
print(numeros_random)

numeros_random.sort(reverse=True)  # Ordena de mayor a menor
print("Lista de números aleatorios ordenados de mayor a menor:")
print(numeros_random)

numeros_random.sort()  # Ordena de menor a mayor
print("Lista de números aleatorios ordenados de menor a mayor:")
print(numeros_random)

# Calculo del promedio
promedio = sum(numeros_random) / len(numeros_random)

# Definimos una función de comparación para ordenar según la distancia al promedio
def distancia_al_promedio(n):
    return abs(n - promedio)

# Ordenamos la lista según la distancia al promedio
numeros_random.sort(key=distancia_al_promedio)

# Imprimimos la lista ordenada según la distancia al promedio
print("Lista de números aleatorios ordenados según la distancia al promedio =", promedio)
print(numeros_random)

i = 0
while i < len(numeros_random):
    print("El elemento en el espacio", i, "de la lista es:", numeros_random[i],
          "y está a una distancia de", abs(numeros_random[i] - promedio), "del promedio:", promedio)
    i += 1

# Sin métodos sort

# Ordenar de mayor a menor manualmente
for i in range(len(numeros_random) - 1):
    for j in range(len(numeros_random) - 1):
        if numeros_random[j] < numeros_random[j + 1]:
            numeros_random[j], numeros_random[j + 1] = numeros_random[j + 1], numeros_random[j]

# Imprimimos la lista ordenada de mayor a menor
print("Lista ordenada de mayor a menor sin utilizar el método sort:")
print(numeros_random)

# Ordenar de menor a mayor manualmente
for i in range(len(numeros_random) - 1):
    for j in range(len(numeros_random) - 1):
        if numeros_random[j] > numeros_random[j + 1]:
            numeros_random[j], numeros_random[j + 1] = numeros_random[j + 1], numeros_random[j]

# Imprimimos la lista ordenada de menor a mayor
print("Lista ordenada de menor a mayor sin utilizar el método sort:")
print(numeros_random)

# Ordenar según la distancia al promedio sin método sort
# Calcular las distancias al promedio
distancias = [(num, abs(num - promedio)) for num in numeros_random]

# Algoritmo de ordenamiento de burbuja personalizado
for i in range(len(distancias) - 1):
    for j in range(len(distancias) - i - 1):
        if distancias[j][1] > distancias[j + 1][1]:
            distancias[j], distancias[j + 1] = distancias[j + 1], distancias[j]

# Extraer los números ordenados
numeros_ordenados = [num for num, _ in distancias]

# Imprimir la lista original, el promedio y la lista ordenada
print("Lista original:", numeros_random)
print("Promedio:", promedio)
print("Lista ordenada por distancia al promedio sin utilizar el método sort:", numeros_ordenados)