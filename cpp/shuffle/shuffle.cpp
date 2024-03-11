#include <iostream>

void ShuffleRows(int **orig, int rows) {
    const int p = 9973;
    int **aux = new int *[rows];
    
    for (int r = 0; r < rows; r++) {
        aux[r] = orig[r];
    }
    
    for(int i=0; i < rows; i++) {
        int newr = (i * p) % rows;
        orig[i] = aux[newr];
    }
    
    delete [] aux;
    aux = nullptr;
}

int main() {
    // Definir el tamaño de la matriz (filas y columnas)
    const int rows = 5;
    const int cols = 3;
    
    // Crear una matriz de números (ejemplo)
    int **matrix = new int *[rows];
    for (int i = 0; i < rows; i++) {
        matrix[i] = new int[cols];
    }
    
    // Rellenar la matriz con valores (por ejemplo)
    int value = 1;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = value++;
        }
    }
    
    // Mostrar la matriz antes del barajeo
    std::cout << "Matriz antes del barajeo:" << std::endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    // Llamar a la función para barajear las filas
    ShuffleRows(matrix, rows);
    
    // Mostrar la matriz después del barajeo
    std::cout << "\nMatriz después del barajeo:" << std::endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
    
    // Liberar la memoria de la matriz
    for (int i = 0; i < rows; i++) {
        delete[] matrix[i];
    }
    delete[] matrix;
    
    return 0;
}
