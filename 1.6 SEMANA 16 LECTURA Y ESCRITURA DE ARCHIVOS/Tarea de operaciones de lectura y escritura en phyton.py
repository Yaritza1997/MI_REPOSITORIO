# Hola bienvenidos al trabajo con Archivos de Texto en Python

# Crear un nuevo archivo llamado my_notes.txt
file = open('my_notes.txt', 'w')  # Abre el archivo en modo de escritura

# Escribir al menos tres líneas de notas personales en el archivo
file.write("Nota 1: El 03 de mayo es mi cumpleaños .\n")
file.write("Nota 2: Me gusta bailar y leer.\n")
file.write("Nota 3: Mi signo sodiacal es Tauro.\n")
file.close()  # Cierra el archivo después de escribir

# Abrir el archivo my_notes.txt
print("Notas Personales:")
file = open('my_notes.txt', 'r')  # Abre el archivo en modo de lectura
# Leer el contenido del archivo línea por línea
for line in file:
    # Mostrar en la consola cada línea leída
    print(line.strip())  # .strip() elimina el salto de línea al final de cada línea
file.close()  # Cierra el archivo después de leer