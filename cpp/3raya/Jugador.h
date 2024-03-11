#ifndef JUGADOR_H
#define JUGADOR_H

#include <string>
#include "Ficha.h"

class Jugador
{
private:
    std::string nombre;
    Ficha ficha;

public:
    Jugador();
    Jugador(std::string nombre, Ficha ficha);
    std::string getNombre();
    Ficha getFicha();
};

#endif