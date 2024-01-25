def nonDivisibleSubset(k, s):
    # Contar la frecuencia de los residuos al dividir por k
    residuo_frecuencia = [0] * k
    for num in s:
        residuo_frecuencia[num % k] += 1

    # Contar el tamaño máximo del subconjunto no divisible
    counter = min(residuo_frecuencia[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            counter += max(residuo_frecuencia[i], residuo_frecuencia[k - i])
        else:
            counter += 1

    return counter


# Ejemplo de uso
k = 7
s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
resultado = nonDivisibleSubset(k, s)
print(resultado)
