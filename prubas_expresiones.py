import re
res = re.search("c", "abcdefc") #esta devuelve un objeto 
print(res)
resultado = re.findall("\s", "esta es una cadena.")#devuelve una lista 
print (resultado)
resultado = re.split("\s", "esta es una cadena.")
print (resultado)
resultado = re.sub("\s", "\n", "esta es una cadena.")
print (resultado)

patron = re.compile(",")
resultado = patron.findall("Cadena1, Cadena2, Cadena3, Cadena4, Cadena5")
print(resultado)
resultado2 = patron.split("Cadena1, Cadena2, Cadena3, Cadena4, Cadena5")
print(resultado2)

patron = re.compile("\d+\.?\d+")
resultado = patron.findall("Esta es una cadena con los números 14, 15.5 y 0.25 0..9")
print(resultado)