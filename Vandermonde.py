
n = 10

# Crear matriz
Matrix = [[0 for x in range(n)] for y in range(n)] 

# Rellenar matriz
for i in range(0, n):
    for j in range(0, n):
        Matrix[i][j] = (i+1)**j

# Mostrar matriz de Vandermonde generada
for i in range(n):
    for j in range(n):
        print(Matrix[i][j], end='\t')
    print()


