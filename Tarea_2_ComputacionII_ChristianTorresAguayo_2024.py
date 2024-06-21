# Christian Torres Aguayo

a = 10  # Guarda el valor de 10 en la variable a
b = "adiós"  # Guarda la cadena de caracteres "adiós" en la variable b
print(a)  # Imprime en pantalla el valor almacenado en la variable a
print(b)  # Imprime en pantalla el valor almacenado en la variable b

a = 15  # Asigna otro valor a la variable a
print(a)  # Imprime en pantalla el nuevo valor almacenado en la variable a

c = a - 2  # Asigna otro valor que depende de a a la variable c
print(c)  # Imprime en pantalla el valor almacenado en la variable c

d = str(7)  # Guarda el carácter "7" en la variable d
e = int(7)  # Guarda el entero "7" en la variable e
f = float(7)  # Guarda el real "7" en la variable f

print("caracter:", d, "es de tipo", type(d), " entero:", e, "es de tipo", type(e), " flotante:", f, "es de tipo", type(f))
# Imprime los valores de las variables d, e y f, añadiendo qué tipo de variable son

v1, v2, v3 = "v1", 4, False  # Asigna valores a variables de manera múltiple

print(v1, v2, v3)  # Imprime los valores almacenados en las variables v1, v2 y v3
# print(v1 + v2 + v3)  # Marca error, no se pueden sumar peras con manzanas, no son el mismo tipo de dato 

vegetales = ["zanahoria", "lechuga", "pepino"]  # Array de 3 elementos con entradas de caracteres
Verduras = [v1, v2, v3]  # Array de 3 elementos con diferentes tipos de entradas
v1, v2, v3 = vegetales  # Guarda cada entrada del array en una variable
print(v1)  # Imprime la primera entrada del array almacenada en la variable v1
print(v2)  # Imprime la segunda entrada del array almacenada en la variable v2
print(v3)  # Imprime la tercera entrada del array almacenada en la variable v3

"""Ejemplo de comentarios múltiples
en el código"""

descrip = "interesante"  # Variable global fuera de la función

def nuevaFuncion():
    # Crear función y nombre de dicha función
    print("Programar en Python es " + descrip)  # Cuerpo de la función tomando una variable global fuera de ella de lo contrario sería local
nuevaFuncion()  # Evalúa y arroja la operación marcada en el cuerpo de la función

def nuevaFuncion():
    # Crear función y nombre de dicha función
    descrip_local = "asombroso"  # Solo funciona dentro de la función, fuera de ella no funcionará ya que tiene un valor local
    print("Programar en Python es " + descrip_local)  # Imprime el valor de la variable local
nuevaFuncion() 

print("Programar en Python es " + descrip)  # Vuelve a escribir el valor de la variable global no local
