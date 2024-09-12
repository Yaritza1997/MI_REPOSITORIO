# Definir la función primero
def calcular_temperatura_promedio(datos):

    # Almacenar los promedios de cada ciudad
    promedios = {}

    # Recorrer cada ciudad y sus temperaturas semanales
    for ciudad, semanas in datos.items():
        temperaturas_semanales = [sum(semana) / len(semana) for semana in semanas]

    # Calcular el promedio total de todas las semanas
        promedio_total = sum(temperaturas_semanales) / len(temperaturas_semanales)

        # Guardar el promedio como resultados
        promedios[ciudad] = promedio_total

    return promedios


# definicion de  los datos por ciudades
temperaturas = {
    'Esmeraldas': [
        # Semana 1
        [20, 21, 22, 23, 24],  # Lunes a Viernes
        # Semana 2
        [25, 26, 27, 28, 29],
        # Semana 3
        [24, 23, 22, 21, 20],
        # Semana 4
        [26, 25, 24, 23, 22]
    ],
    'Santo Domingo': [
        # Semana 1
        [15, 16, 17, 18, 19],
        # Semana 2
        [20, 21, 22, 23, 24],
        # Semana 3
        [19, 18, 17, 16, 15],
        # Semana 4
        [22, 21, 20, 19, 18]
    ],
    'Quito': [
        # Semana 1
        [10, 12, 14, 13, 15],
        # Semana 2
        [16, 18, 20, 22, 24],
        # Semana 3
        [14, 13, 12, 11, 10],
        # Semana 4
        [18, 17, 16, 15, 14]
    ]
}

# Calcular el promedio de temperaturas
promedios = calcular_temperatura_promedio(temperaturas)

# Mostrar el promedio de temperaturas con °C
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.1f}°C")