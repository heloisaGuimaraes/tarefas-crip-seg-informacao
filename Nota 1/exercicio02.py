import numpy as np
size = 4

def code(matrix, key=2):

    for i in range(4):
      matrix[i] = np.transpose(matrix[i])
      for j in range(4):
        for k in range(4):
          (matrix[i])[j][k] = ((matrix[i])[j][k])+key
    return matrix

  

key = int(input('Entre com a chave (numero inteiro): '))
matrix = np.array(
  [[[0, 1, 0, 2],
   [0, 1, 0, 2],
   [0, 1, 0, 2],
   [0, 1, 0, 2]],
  
  [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [0, 0, 0, 0],
   [2, 2, 2, 2]], 
  
  [[0, 1, 0, 2],
   [0, 1, 0, 2],
   [0, 1, 0, 2],
   [0, 1, 0, 2]],
  
 [[0, 0, 0, 0],
   [1, 1, 1, 1],
   [0, 0, 0, 0],
   [2, 2, 2, 2]]])

print('Matriz codificada:\n ', code(matrix, key))
#para decodificar basta passar a chave com valor negativo
print('\nMatriz decodificada:\n ', code(matrix, -key))
