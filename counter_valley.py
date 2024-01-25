def countingValleys(steps, path):
    # Write your code here
    bandera = False
    counter = 0
    posicion = 0
    lista = [i for i in path]
    
    for i in lista:
        if i == "D" and posicion == 0:
             bandera = True
             posicion -= 1
        elif i == "U" and bandera:
            posicion += 1
            if posicion == 0:
                counter += 1
                bandera = False
        elif i == "D" and posicion < 0:
            posicion -= 1
        elif i == "D" and posicion >= 0:
            posicion -= 1 
        elif i == "U" and posicion >= 0:
            posicion += 1
    return counter

path = "UDDDUDUU"
print(countingValleys(8, path))