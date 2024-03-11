#include <cassert>
#include "Tablero.h"

Tablero::Tablero()
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            tablero[i][j] = BLANCO;
        }
    }
    colocadas = 0;
}

void Tablero::colocar(int fila, int columna, Ficha ficha)
{
    assert((fila < 3) && (fila >= 0) && (columna < 3) && (columna >= 0) && (tablero[fila][columna] == BLANCO));
    tablero[fila][columna] = ficha;
    colocadas++;
}

bool Tablero::check3enRaya()
{
    // Filas
    for (int fila = 0; fila < 3; fila++)
    {
        if (tablero[fila][0] != BLANCO && tablero[fila][0] == tablero[fila][1] && tablero[fila][1] == tablero[fila][2])
            return true;
    }

    // Columnas
    for (int columna = 0; columna < 3; columna++)
    {
        if (tablero[0][columna] != BLANCO && tablero[0][columna] == tablero[1][columna] && tablero[1][columna] == tablero[2][columna])
            return true;
    }

    // Diagonales
    if (tablero[0][0] != BLANCO && tablero[0][0] == tablero[1][1] && tablero[1][1] == tablero[2][2])
        return true;

    if (tablero[0][2] != BLANCO && tablero[0][2] == tablero[1][1] && tablero[1][1] == tablero[2][0])
        return true;

    return false;
}

Ficha Tablero::getFichaEn(int fila, int columna)
{
    return tablero[fila][columna];
}

int Tablero::getColocadas()
{
    return colocadas;
}

std::ostream &operator<<(std::ostream &salida, Tablero tablero)
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            salida << tablero.getFichaEn(i, j);
        }
        salida << std::endl;
    }
    return salida;
}