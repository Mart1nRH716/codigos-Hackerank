from collections import Counter


def migratoryBirds(arr):
    # Write your code here
    conteo = Counter(arr)
    frecuecias = conteo.most_common(5)
    sorted(frecuecias)
    tuplas_ordenadas = sorted(frecuecias, key=lambda x: (x[1], x[0]), reverse= True)
    id_rep = tuplas_ordenadas[0][0]
    for i in tuplas_ordenadas[1:]:
        if tuplas_ordenadas[0][1] == i[1] and tuplas_ordenadas[0][0] > i[0]:
            id_rep = i[0]
    return id_rep


11
arr = [1, 2, 4, 3, 5, 4, 3, 2, 1, 3, 4]
print(migratoryBirds(arr))