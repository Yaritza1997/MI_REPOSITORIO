# Definicion de matriz bidimensional 3x3
matriz =[
    [ 5, 15, 8],
    [30, 7, 40],
    [10, 50, 33],
]
print(matriz)

# Busqueda de un valor especìfico

def buscar(matriz, elemento_de_interes):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz [i][j] == elemento_de_interes:
                return i,j
elemento_de_interes = 40

# Mensaje de respuesta
print("Resultado de la posicion:", buscar(matriz,elemento_de_interes))

if elemento_de_interes == elemento_de_interes :
    print( "Valor ubicado correctamente")
else:
    print("Valor ubicado incorrecto ")
