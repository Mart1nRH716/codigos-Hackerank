'''
Farmer:
A Farmer wants to farm their land …
Please help the Farmer to find maximum area of the land they can farm in good land
'''

import copy
def maximum_square(matrix) -> int :
	m_aux = copy.deepcopy(matrix) #O(N*m)
	max_number = 1
	for i in range(0, len(matrix)): #rows
		for j in range(0,len(matrix[0])): #columns #O(N*m)
			if matrix[i][j] != 0:
				if i - 1 >= 0 and j - 1 >= 0:
					if matrix[i-1][j] > 0 and matrix[i][j-1] > 0 and matrix[i-1][j-1] > 0:
						m_aux[i][j] = min(m_aux[i-1][j], m_aux[i][j-1], m_aux[i-1][j-1]) + 1
						max_number = max(m_aux[i][j], max_number)
			# else:
			# 	m_aux[i][j]	= 0
			
	return max_number

matrix = [
	[0,1,1,0,1],
	[1,1,1,1,1],
	[0,1,1,1,1],
	[1,1,1,1,1],
	[1,1,1,1,1],
	[0,0,0,0,0]
]

print(maximum_square(matrix)) 
m = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(maximum_square(m)) 