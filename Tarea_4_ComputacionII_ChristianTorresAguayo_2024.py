# Christian Torres Aguayo

txt = "La programación es una habilidad esencial en la era digital"  # Cadena de caracteres almacenada en la variable txt

print("programación" in txt)  # Imprime un valor booleano si la palabra se encuentra en la cadena guardada en txt, da True
print("matemáticas" in txt)  # Da False

if "programación" in txt:  # Condicional evalúa el valor booleano y realiza la acción de imprimir
    print("1- Efectivamente la palabra 'programación' está en la frase:", txt)
    if "matemáticas" not in txt:  # Condicional anidado evalúa la negación de algo falso que da True e imprime el mensaje
        print("2- Las matemáticas son otra área importante")

a = "987654321"  # Cadena almacenada en a

print(a[:len(a)])  # Imprime los valores de la cadena desde el valor inicial hasta el final
print(a[5:9])  # Imprime solo un rango de los últimos 4 valores de la palabra
print(a[0:])  # Imprime desde el primer valor hasta el final
print(a[-4:])  # Imprime los últimos 4 valores
print(a[-len(a):])  # Imprime toda la palabra

b = "minúsculas"  # Palabra en minúsculas almacenada en la variable b
c = b.upper()  # Guarda en c las letras a las que se les aplica el método para transformar minúsculas a mayúsculas
print(c)  # Imprime la palabra en mayúsculas

e = "MAYÚSCULAS"  # Mismo caso de arriba pero de mayúsculas a minúsculas
f = e.lower()
print(f)

s = "    espacios adicionales    "  # Palabra con espacios extras en los extremos
t = s.strip()  # Método para quitar los espacios en los extremos
print("Imprime con espacios:", s, "imprime sin espacios:", t)  # Imprime ambos casos, con espacios y sin espacios

y = "tecnología"  # Una palabra a modificar
z = y.replace("o", "a")  # Aplica el método para modificar strings, reemplaza letras incorrectas por las correctas
print("Está mal:", y, "está bien escrita:", z)  # Imprime ambos ejemplos

partir = "uno,dos,tres,cuatro,cinco"  # String separada por comas
partido = partir.split(",")  # Parte la cadena en el símbolo ","
print(partido)  # Imprime un array de las separaciones que marca el símbolo
print("Al partir con el método split la cadena separada por comas creo un array de tamaño", len(partido))  # Imprime el tamaño de dicho array

calificacion = 9  # Variable
texto = "Me saqué un {}"  # Las {} son un comodín para el método format
print(texto.format(calificacion))  # Imprime el texto con el valor almacenado usando el método format

n, m, l = 4, 5, 6
numeros = "El primer número es: {} el segundo es: {} el tercero es: {}"  # Manera de concatenar más eficiente que usando ","
print(numeros.format(n, m, l))  # Procurar poner los argumentos del método de manera correcta

numerosDesordenados = "El tercer número es: {2} el primero es: {0} el segundo es: {1}"  # Concatenación ordenando de distintas maneras
print(numerosDesordenados.format(n, m, l))  # Ordenados
