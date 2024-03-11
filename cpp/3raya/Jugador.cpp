#include "Jugador.h"

Jugador::Jugador() {}

Jugador::Jugador(std::string nombre, Ficha ficha) : nombre(nombre), ficha(ficha) {}

std::string Jugador::getNombre()
{
    return nombre;
}

Ficha Jugador::getFicha()
{
    return ficha;
}