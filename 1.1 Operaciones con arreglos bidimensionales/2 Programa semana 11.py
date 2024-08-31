# Definicion de matriz bidimensional 4x3
matriz =[
    [85, 92, 78],
    [88, 76, 91],     #FILA A ORDENAR
    [79, 85, 84],
    [90, 87, 93],      #FILA A OREDENAR
]
print ("Matriz Original:", matriz)


# Empleamos metodo de ordenamiento QuickSort
def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)


 # Identificacion de la fila que deseo ordenar
fila_a_ordenar = [1,3]


 # Ejecucion de las filas ya ordenadas
for fila in fila_a_ordenar:
    matriz[fila] = quicksort(matriz[fila])

print ("Matriz Ordenada:", matriz)

