#ifndef TABLERO_H
#define TABLERO_H

#include "Ficha.h"

class Tablero
{
private:
    Ficha tablero[3][3];
    int colocadas;
public:
    Tablero();
    void colocar(int fila, int columna, Ficha ficha);
    Ficha getFichaEn(int fila, int columna);
    int getColocadas();
    bool check3enRaya();
};

std::ostream &operator<<(std::ostream &salida, const Tablero tablero);

#endif