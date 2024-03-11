#include "Ficha.h"

std::ostream &operator<<(std::ostream &salida, const Ficha ficha)
{
    if (ficha == BLANCO)
        salida << "   ";
    else if (ficha == CIRCULO)
        salida << " O ";
    else
        salida << " X ";
    return salida;
}
