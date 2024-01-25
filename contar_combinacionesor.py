from collections import Counter


def or_binario(binario1, binario2):
    lista = ['1' if (bin1 == '1' or bin2 == "1") else '0' for bin1, bin2 in zip(binario1, binario2)]
    return lista

def contar(lista_tuplas, max_freq):
    counter = 0
    for i in lista_tuplas:
        if i[1] == max_freq:
            counter += 1
    return counter
    
    
def acmTeam(topic):
    x = 0
    y = 1
    max_freq = 0
    lista_tuplas = []
    while (x < len(topic) and y < len(topic)):
        lista = or_binario(topic[x], topic[y])
        contador = Counter(lista)
        frecuencia = contador["1"]
        tupla = (x, y)
        lista_tuplas.append((tupla, frecuencia))
        if max_freq < frecuencia:
            max_freq = frecuencia
        y += 1
        if y == len(topic):
            x += 1
            y = x + 1
        
    return max_freq, contar(lista_tuplas, max_freq)

topic = ["10101", "11100", "11010", "00101"]
print(acmTeam(topic))