# Christian Torres Aguayo

# Guardamos en la variable archivo el archivo de texto Archivo2.txt
archivo = open("C:\\Users\\chris\\Fisica-Mat\\Mis Tareas Compu 2\\Archivo2.txt", "rt", encoding="utf-8")  # Abrir el archivo Archivo2.txt en modo lectura con codificación UTF-8
print(archivo.read())  # Leer y imprimir todo el contenido del archivo
archivo.close()  # Cerrar el archivo

print()

# Guardamos en la variable ruta el archivo de texto Ruta.txt
ruta = open("C:\\Users\\chris\\Fisica-Mat\\Mis Tareas Compu 2\\Ruta.txt", encoding="utf-8")  # Abrir el archivo Ruta.txt en modo lectura con codificación UTF-8
print(ruta.read())  # Leer y imprimir todo el contenido del archivo
ruta.close()  # Cerrar el archivo

print()

# Guardamos en la variable archivo2 el archivo de texto Ar.txt
archivo2 = open("C:\\Users\\chris\\Fisica-Mat\\Mis Tareas Compu 2\\Ar.txt", "rt", encoding="utf-8")  # Abrir el archivo Ar.txt en modo lectura con codificación UTF-8
lineas = archivo2.readlines()  # Leer todas las líneas del archivo y almacenarlas en una lista

print(lineas)  # Imprimir la lista de líneas
print("La variable lineas es de tipo", type(lineas))  # Imprimir el tipo de la variable 'lineas'
print("El número de líneas es", len(lineas))  # Imprimir el número de líneas en el archivo

for l in lineas:
    if l == lineas[7]:  # Verificar si la línea actual es la línea 8 (índice 7)
        print("Se cumplió la condición")
        linea8 = lineas[7]
        print(f"La línea 8 se imprime y es: {lineas[7]}")
    else:
        print(f"La línea {l.strip()} no se imprime ")  # Imprimir las líneas que no son la línea 8
archivo2.close()  # Cerrar el archivo

