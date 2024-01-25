import random


def diagonalDifference(arr):
    x = 0
    y  = 0
    for i in range(len(arr)):
        for j in range(len(i)):
            if (i == j):
                x += arr[i][j]


def generar_matriz_aleatoria(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            # Generar un número aleatorio entre 1 y 100 (puedes ajustar el rango según tus necesidades)
            numero_aleatorio = random.randint(1, 100)
            fila.append(numero_aleatorio)
        matriz.append(fila)
    return matriz

# Ejemplo de uso:
n = 3 # Cambia este valor al tamaño de matriz que desees
matriz_aleatoria = generar_matriz_aleatoria(n)

for linea in matriz_aleatoria:
    print (linea)
x = -1
i = len(matriz_aleatoria)
for t in range(i):
    print(f'Matriz[{t}][{t}] = {matriz_aleatoria[t][t]}')
    print(f'Matriz[{t}][{x}] = {matriz_aleatoria[t][x]}')
    x -= 1