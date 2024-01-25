def kaprekarNumbers(p, q):
    # Write your code here
    lista = []
    for i in range(p, q + 1):
        number = str((i ** 2))
        if len(number) == 1:
            if number == i:
                lista.append(i)
        else:
            indice_superior = len(number)//2
            mitad_1 = number[0:indice_superior]
            mitad_2 = number[indice_superior:]
            if int(mitad_1) + int(mitad_2) == i:
                lista.append(i)
    return lista

print(kaprekarNumbers(1, 100))