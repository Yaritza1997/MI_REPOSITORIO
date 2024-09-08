# DEFINICION DE MATRIZ 3D CON VARIAS TEMPERATURAS
# 3 ciudades
# 3 semanas
# 5 dias

temperaturas = [
    # Ciudad 1
    [
        # Semana 1
        [20, 21, 22, 23, 24],  # Lunes a Viernes
        # Semana 2
        [25, 26, 27, 28, 29],
        # Semana 3
        [24, 23, 22, 21, 20],
        # Semana 4
        [26, 25, 24, 23, 22]
    ],
    # Ciudad 2
    [
        # Semana 1
        [15, 16, 17, 18, 19],
        # Semana 2
        [20, 21, 22, 23, 24],
        # Semana 3
        [19, 18, 17, 16, 15],
        # Semana 4
        [22, 21, 20, 19, 18]
    ],
    # Ciudad 3
    [
        # Semana 1
        [10, 12, 14, 13, 15],
        # Semana 2
        [16, 18, 20, 22, 24],
        # Semana 3
        [14, 13, 12, 11, 10],
        # Semana 4
        [18, 17, 16, 15, 14]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por semana
# Recorrer las ciudades
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")

    # Recorrer las semanas para la ciudad actual
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)  # Calcular el promedio de la semana
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}")