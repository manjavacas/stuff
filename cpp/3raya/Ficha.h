#ifndef FICHA_H
#define FICHA_H

#include <iostream>

enum Ficha
{
    CIRCULO,
    CRUZ,
    BLANCO
};

std::ostream &operator<<(std::ostream &salida, Ficha ficha);

#endif