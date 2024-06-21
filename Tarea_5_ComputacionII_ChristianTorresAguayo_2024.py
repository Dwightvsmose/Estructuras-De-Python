# Christian Torres Aguayo

a = 12
b = 8

if a - 3 > b:
    print("esto es verdad")  # Operaciones con operadores en condicionales siempre y cuando sea verdadero
else:
    print("esto es falso")  # Si la tesis es falsa, ejecuta esta parte del código

x = 15
y = 30

c = y % x  # 30 módulo 15 guardado en la variable c = 0

print(c)
if c < x:
    print("este valor no es divisible entre 15")  # Imprime si la tesis es verdadera

t = 2
s = 5
k = 7

if t < s and s < k:
    print("esto es verdadero")  # Condicionales con operadores lógicos (V and V = V)
else:
    print("esto es falso")

if t < s < k:
    print("verdad")
if t < s or s > k:
    print("verdad y equivalente")

#g = int(input("dame un entero"))
#f = int(input("dame otro entero"))

#if g == f:
    #print("g = {} es igual a f = {}".format(g, f))

EscalaSolMayor = ["sol", "la", "si", "do", "re", "mi", "fa#"]  # Lista de 7 elementos tipo str

print(EscalaSolMayor)
print("El número de notas de la escala de Sol Mayor es =", len(EscalaSolMayor))  # Imprime el tamaño de la lista

if EscalaSolMayor[0] == "sol" and EscalaSolMayor[2] == "si" and EscalaSolMayor[4] == "re":  # Compara los elementos de la lista y si cumple la condición realiza la sentencia
    Gmayor = [EscalaSolMayor[0], EscalaSolMayor[2], EscalaSolMayor[4]]
    print("Este es el acorde de Sol Mayor", Gmayor, "que consta de", len(Gmayor), "notas")

EscalaSolMayor[0], EscalaSolMayor[2], EscalaSolMayor[4] = "la", "do#", "mi"  # Asignar otro valor a las i-ésimas entradas de la lista

Amayor = [EscalaSolMayor[0], EscalaSolMayor[2], EscalaSolMayor[4]]  # Crear una nueva lista con los valores seteados

print("Este es el acorde de La mayor:", Amayor)  # Imprime los nuevos valores

if "sol#" in EscalaSolMayor:  # Sentencia para verificar elementos específicos de la lista
    print("Tenemos una escala exótica")  # Condición que no se cumplirá
else:
    print("Esta nota no pertenece a la tonalidad")  # Condición que se cumple

CerosYUnos = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1]  # Lista de 0 y unos
print("La lista es esta:", CerosYUnos, "y su tamaño es", len(CerosYUnos))

CerosYUnos.insert(0, 0)  # Insertar un nuevo valor al espacio 0 de la lista
print("La nueva lista es:", CerosYUnos, "y su tamaño es", len(CerosYUnos))
