def heapsort(arr):
    # Función para construir un max-heap.
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar los elementos.
            heapify(arr, n, largest)

    # Construir el max-heap.
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno del max-heap.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el elemento máximo con el último.
        heapify(arr, i, 0)

# Ejemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Arreglo ordenado:")
print(arr)