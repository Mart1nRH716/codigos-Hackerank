#En esta hay que mandar solo la lista que contiene el obstaculo en la fila y direccion que se cuenta
def contar_arriba(n, r_q, c_q,  obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if r_q >= n:
            return counter
        else:
            return contar_arriba(n, r_q+1 , c_q, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if r_q >= n or (obstaculo_colA[0] == r_q + 1 and obstaculo_colA[1] == c_q):
            return counter
        else:
            return contar_arriba(n, r_q + 1, c_q, obstaculo_colA, counter + 1)
        
def contar_abajo(n, r_q, c_q, obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if r_q <= 1:
            return counter
        else:
            return contar_abajo(n, r_q-1, c_q, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if r_q <= 1 or  (obstaculo_colA[0] == r_q - 1 and obstaculo_colA[1] == c_q):
            return counter
        else:
            return contar_abajo(n, r_q - 1, c_q , obstaculo_colA, counter + 1)
        
def contar_izq(n, r_q, c_q, obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if c_q <= 1:
            return counter
        else:
            return contar_izq(n, r_q, c_q-1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if c_q <= 1 or  (obstaculo_colA[1] == c_q - 1 and obstaculo_colA[0] == r_q):
            return counter
        else:
            return contar_izq(n, r_q, c_q - 1, obstaculo_colA, counter + 1)
        
def contar_der(n, r_q, c_q, obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if c_q >= n:
            return counter
        else:
            return contar_der(n, r_q, c_q+1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if c_q >= n or (obstaculo_colA[1] == c_q + 1 and obstaculo_colA[0] == r_q):
            return counter
        else:
            return contar_der(n, r_q, c_q + 1, obstaculo_colA, counter + 1)
############################################################################       
def contar_diag_derecha_arriba(n, r_q, c_q,  obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if r_q >= n or c_q >= n:
            return counter
        else:
            return contar_diag_derecha_arriba(n, r_q+1, c_q+1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if r_q >= n or c_q >= n or (obstaculo_colA[0] == r_q + 1 and obstaculo_colA[1] == c_q + 1):
            return counter
        else:
            return contar_diag_derecha_arriba(n, r_q+1, c_q+1, obstaculo_colA, counter + 1)
        
def contar_diag_izq_arriba(n, r_q, c_q,  obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if r_q >=  n or c_q <= 1:
            return counter
        else:
            return contar_diag_izq_arriba(n, r_q+1, c_q -1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if r_q >= n or c_q <= 1 or (obstaculo_colA[0] == r_q + 1 and obstaculo_colA[1] == c_q - 1):
            return counter
        else:
            return contar_diag_izq_arriba(n, r_q+1, c_q - 1, obstaculo_colA, counter + 1)
        
def contar_diag_derecha_abajo(n, r_q, c_q,  obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if c_q >=  n or r_q <= 1:
            return counter
        else:
            return contar_diag_derecha_abajo(n, r_q-1, c_q+1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if c_q >=  n or r_q <= 1 or (obstaculo_colA[0] == r_q - 1 and obstaculo_colA[1] == c_q + 1):
            return counter
        else:
            return contar_diag_derecha_abajo(n, r_q-1, c_q+1, obstaculo_colA, counter + 1)
        
def contar_diag_izq_abajo(n, r_q, c_q,  obstaculo_colA, counter):
    if len(obstaculo_colA) == 0:
        if r_q <=  1 or c_q <= 1:
            return counter
        else:
            return contar_diag_izq_abajo(n, r_q-1, c_q -1, obstaculo_colA, counter + 1)
    else:
        #Esto se hace para que no avance al otro lado
        if r_q <= 1 or c_q <= 1 or (obstaculo_colA[0] == r_q - 1 and obstaculo_colA[1] == c_q - 1):
            return counter
        else:
            return contar_diag_izq_abajo(n, r_q-1, c_q - 1, obstaculo_colA, counter + 1)

def obt_obstaculo_arriba (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q < obstaculo[0] and c_q == obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_abajo (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q > obstaculo[0] and c_q == obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_izq (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q == obstaculo[0] and c_q > obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_derecha (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q == obstaculo[0] and c_q < obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_diag_arriba_der (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q < obstaculo[0] and c_q < obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_diag_arriba_izq (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q < obstaculo[0] or c_q > obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_diag_abajo_der (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q > obstaculo[0] or c_q < obstaculo[1]:
            return obstaculo
    return []
def obt_obstaculo_diag_abajo_izq (r_q, c_q,  obstaculo_colA):
    for obstaculo in obstaculo_colA:
        if r_q > obstaculo[0] or c_q > obstaculo[1]:
            return obstaculo
    return []

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obst_arr = obt_obstaculo_arriba(r_q, c_q, obstacles)
    obst_aba = obt_obstaculo_abajo(r_q, c_q, obstacles)
    obst_izq = obt_obstaculo_izq(r_q, c_q, obstacles)
    obst_der = obt_obstaculo_derecha(r_q, c_q, obstacles)
    obst_diag_arr_der = obt_obstaculo_diag_arriba_der(r_q, c_q, obstacles)
    obst_diag_arr_izq = obt_obstaculo_diag_arriba_izq(r_q, c_q, obstacles)
    obst_diag_abajo_der = obt_obstaculo_diag_abajo_der(r_q, c_q, obstacles)
    obst_diag_abajo_izq = obt_obstaculo_diag_abajo_izq(r_q, c_q, obstacles)
    
    return contar_arriba(n, r_q, c_q, obst_arr, 0) + contar_abajo(n, r_q, c_q, obst_aba, 0) + contar_izq(n, r_q, c_q, obst_izq, 0) + contar_der(n, r_q, c_q, obst_der, 0) + contar_diag_derecha_arriba(n, r_q, c_q, obst_diag_arr_der, 0) +contar_diag_izq_arriba(n, r_q, c_q, obst_diag_arr_izq, 0) + contar_diag_derecha_abajo(n, r_q, c_q, obst_diag_abajo_der, 0) + contar_diag_izq_abajo(n, r_q, c_q, obst_diag_abajo_izq, 0)

# print(contar_arriba(5, 4, 3 , [], 0))
# print(contar_abajo(5, 4, 3 , [2,3], 0))
# print(contar_izq(5, 4, 3 , [4,2], 0))
# print(contar_der(5, 4, 3 , [], 0))

# print(contar_diag_izq_abajo(5, 4, 3 , [], 0))
# print(contar_diag_derecha_abajo(5, 4, 3 , [], 0))
# print(contar_diag_izq_arriba(5, 4, 3 , [], 0))
# print(contar_diag_derecha_arriba(5, 4, 3 , [], 0))

print (queensAttack(5, 0, 4, 3, [[5, 5], [4, 2], [2,3]]))