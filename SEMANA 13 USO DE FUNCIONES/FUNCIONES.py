def calcular_temperatura_promedio(datos):
    """
    Calcula el promedio de las temperaturas de cada ciudad.

    Parámetros:
    datos (dict): Diccionario con los nombres de las ciudades como claves y las temperaturas semanales como valores.

    Retorna:
    dict: Diccionario con las ciudades y sus promedios.
    """
    # Almacenar los promedios de cada ciudad
    promedios = {}

    # Recorrer cada ciudad y sus temperaturas semanales
    for ciudad, semanas in datos.items():
        temperaturas_semanales = [sum(semana) / len(semana) for semana in semanas]
    # Calcular el promedio total de todas las semanas
        promedio_total = sum(temperaturas_semanales) / len(temperaturas_semanales)
    # Guardar el promedio como resultado
        promedios[ciudad] = promedio_total

    return promedios


# Definir los datos por ciudades
temperaturas = {
    'Esmeraldas': [
        [20, 21, 22, 23, 24],  # Semana 1
        [25, 26, 27, 28, 29],  # Semana 2
        [24, 23, 22, 21, 20],  # Semana 3
        [26, 25, 24, 23, 22]  # Semana 4
    ],
    'Santo Domingo': [
        [15, 16, 17, 18, 19],  # Semana 1
        [20, 21, 22, 23, 24],  # Semana 2
        [19, 18, 17, 16, 15],  # Semana 3
        [22, 21, 20, 19, 18]  # Semana 4
    ],
    'Quito': [
        [10, 12, 14, 13, 15],  # Semana 1
        [16, 18, 20, 22, 24],  # Semana 2
        [14, 13, 12, 11, 10],  # Semana 3
        [18, 17, 16, 15, 14]  # Semana 4
    ]
}

# Obtener los promedios de las ciudades
promedios = calcular_temperatura_promedio(temperaturas)

# Ciclo interactivo
while True:
    print("Seleccione una ciudad:")
    print("1 - Esmeraldas")
    print("2 - Santo Domingo")
    print("3 - Quito")
    print("0 - Salir")

    opcion = input("Ingrese la opción: ")

    if opcion == '0':
        print("Saliendo del programa...")
        break

    ciudades = ['Esmeraldas', 'Santo Domingo', 'Quito']

    if opcion in ['1', '2', '3']:
        ciudad_seleccionada = ciudades[int(opcion) - 1]
        print(f"La temperatura promedio de {ciudad_seleccionada} es {promedios[ciudad_seleccionada]:.2f}°C")
    else:
        print("Opción inválida. Intente nuevamente.")