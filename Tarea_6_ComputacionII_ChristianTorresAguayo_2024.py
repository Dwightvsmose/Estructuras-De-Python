#Christian Torres Aguayo
print("Lista de 3 elementos:", lista)

lista.append("w")  # Añade un elemento al final de la lista
print("Lista de 4 elementos:", lista)

lista = ["x", "y", "z"]
print("Lista de 3 elementos nuevamente:", lista)
lista.insert(len(lista), "w")  # Inserta un elemento al final de la lista
print("Lista de 4 elementos con otro método:", lista)

l1 = ["10", "20", "30"]
l2 = ["40", "50"]  # Combina listas l1 y l2 usando el método extend
print("Lista l1 =", l1)
print("Lista l2 =", l2)
l1.extend(l2)
print("Lista combinada l1 y l2 =", l1)

a1 = ["pera", "manzana", "uva"]
a2 = ("naranja", "limón")
a1.extend(a2)  # Combina una lista con otros elementos iterables
print("Combinando lista con otros elementos iterables =", a1)

# Operaciones de eliminación en listas
x = ["x", "y", "z"]
print("Lista de 3 elementos:", x)
x.remove("y")  # Elimina un elemento específico de la lista
print("Lista después de eliminar 'y':", x)

y = ["m", "n", "o"]
print("Lista de 3 elementos:", y)
y.pop(1)  # Elimina el elemento en el índice 1
print("Lista después de eliminar el elemento en el índice 1:", y)
del y[0]  # Elimina el primer elemento
print("Lista después de eliminar el primer elemento:", y)

k = ["item1", "item2", "item3"]
print("Lista k:", k)
k.clear()  # Elimina todos los elementos de la lista
print("Lista k después de usar clear():", k)

# Bucles y Condicionales
loop = ["100", "200", "300"]
print("Elementos de la lista:")
for i in loop:  # Imprime cada elemento de la lista
    print(i, end=" ")

loop2 = ["1", "2", "3"]
print()
for i in range(len(loop2)):  # Imprime cada elemento y su índice
    print("Elemento número", i, "de la lista es:", loop2[i])

# Uso de while loop
loop3 = ["a", "b", "c"]
i = 0
while i < len(loop3):  # Imprime cada elemento y su índice usando while
    print("El elemento en el espacio", i, "de la lista es:", loop3[i])
    i += 1

# Filtrado de listas
numeros = ["100", "101", "110", "200", "202"]
conUno = []
print("Lista de números:", numeros)

for i in numeros:  # Filtra elementos que contienen el dígito '1'
    if "1" in i:
        conUno.append(i)
print("Elementos que contienen el dígito '1':", conUno)

conDos = [x for x in conUno if "2" in x]  # Filtra elementos que contienen el dígito '2'
print("De la lista nueva con '1', ahora elementos que contienen el dígito '2':", conDos)

# Función personalizada para ordenar números
def funcion(n):
    return abs(n - 75)

Numeros = [150, 75, 90, 120, 35]
print("Lista de elementos para ordenar:", Numeros)
Numeros.sort(key=funcion)  # Ordena la lista según la distancia al número 75
print("Elementos ordenados según la distancia más corta al número 75:", Numeros)

