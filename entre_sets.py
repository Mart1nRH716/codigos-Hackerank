import math

def calcular_gcd(lista):
    gcd_resultado = lista[0]
    for numero in lista[1:]:
        gcd_resultado = math.gcd(gcd_resultado, numero)
    return gcd_resultado

def calcular_mcm(lista):
    mcm_resultado = lista[0]
    for numero in lista[1:]:
        mcm_resultado = mcm_resultado * numero // math.gcd(mcm_resultado, numero)
    return mcm_resultado

def getTotalX(a, b):
    saltos = calcular_gcd(a)
    multiplo = calcular_mcm(a)
    maximo_num = b[0]
    
    numeros = 0
    for i in range(max(a), maximo_num + 1, saltos):
        for j in range(len(b)):
            if b[j] % i != 0 or i % multiplo != 0:
                break
            if j + 1 == len(b):
                numeros += 1
    return numeros

a = [3, 4]
b = [24, 48]
resultado = getTotalX(a, b)
print(f"La cantidad de números enteros que son divisibles por ambas listas es: {resultado}")