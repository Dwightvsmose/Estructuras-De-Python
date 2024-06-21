# Christian Torres Aguayo

import random

# Asignación de valores enteros, flotantes y complejos a variables
x = 7
y = 3.14
z = 5j
print(x, y, z)  # Imprimir los valores y el tipo de variable que es
print(type(x))
print(type(y))
print(type(z))

# Notación científica
a = 6.022e23
print(a)
print(type(a))

# Números complejos con su parte real e imaginaria
w = 2 + 3j
print(w)
print(type(w))

# Conversión de variables a otro tipo
t = 5
g = 7.8
z = 3 + 4j

l = float(t)
p = int(g)
r = complex(t)

print(l)
print(p)
print(r)

print(type(l))
print(type(p))
print(type(r))

# Generar un número aleatorio en un rango determinado sin incluir el último valor
print(random.randrange(10, 20))

# Cadenas de caracteres
uno = str(3)
dos = str(4)

print(uno, dos)
print(type(uno))
print(type(dos))

# La palabra "mundo" crea un array con la cadena de caracteres donde puedo acceder a cualquier elemento del array
mundo = "mundo"
print(mundo[0], mundo[1], mundo[2], mundo[3], mundo[4])  # Imprimir los caracteres guardados en el array "mundo"

# Función len para obtener el número de caracteres
print("La palabra tiene", len("supercalifragilisticoespialidoso"), "letras")
for i in "supercalifragilisticoespialidoso":
    print(i, end="-")
print()

# Ejercicio de clase
v = "aceleración"
for i in v:
    print(i, end=" ")  # Imprimir los caracteres guardados en el array "v"
print()
print("v almacena", len(v), "letras")

for i in range(len(v)):  # Obtener las entradas del arreglo "v"
    print(v[i], end=" ")
print()
