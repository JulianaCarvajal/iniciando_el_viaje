"""La siguiente matriz (o lista con listas anidadas) debe cumplir que el
cuarto elemento de cada fila se la suma de los tres primeros elementos de
la fila respectiva. Si nota las sumas que se encuentran están erróneas,
debe modificarlas dando 2 soluciones, una con append y otra con slicing.

Ayuda: la función sum(lista) devuelve la suma de todos los elementos de la lista.

Matriz errónea:
matriz = [
    [2, 4, 3, 6],
    [8, 3, 4, 5],
    [7, 1, 3, 10],
    [9, 2, 1, 4]
    ]
    
Debes llegar a:
matriz =[
    [2, 4, 3, 9],
    [8, 3, 4, 15],
    [7, 1, 3,11],
    [9, 2, 1, 12]
    ]
"""

# Append solution:

matriz_append = [
    [2, 4, 3, 6],
    [8, 3, 4, 5],
    [7, 1, 3, 10],
    [9, 2, 1, 4]
    ]

matriz_append[0].pop()
matriz_append[0].append(sum(matriz_append[0]))

matriz_append[1].pop()
matriz_append[1].append(sum(matriz_append[1]))

matriz_append[2].pop()
matriz_append[2].append(sum(matriz_append[2]))

matriz_append[3].pop()
matriz_append[3].append(sum(matriz_append[3]))

print(matriz_append)

# Slicing solution:
matriz_slicing = [
    [2, 4, 3, 6],
    [8, 3, 4, 5],
    [7, 1, 3, 10],
    [9, 2, 1, 4]
    ]

matriz_slicing[0][3] = sum(matriz_slicing[0][:3])

matriz_slicing[1][3] = sum(matriz_slicing[1][:3])

matriz_slicing[2][3] = sum(matriz_slicing[2][:3])

matriz_slicing[3][3] = sum(matriz_slicing[3][:3])

print(matriz_slicing)
