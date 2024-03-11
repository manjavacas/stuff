#include <iostream>
#include "Partida.h"
#include "Ficha.h"

Partida::Partida(std::string nombre1, std::string nombre2) : jugador1(nombre1, CIRCULO), jugador2(nombre2, CRUZ), tablero() {}

void Partida::jugar()
{
    int fila, columna;
    int turno = 0;

    Jugador jugadores[2] = {jugador1, jugador2};
    Jugador jugadorActual;

    bool seguir = true;

    while (seguir)
    {
        jugadorActual = jugadores[turno % 2];

        std::cout << '\n'
                  << std::string(30, '-') << "\n> Turno de " << jugadorActual.getNombre() << std::endl;

        std::cout << "> Introducir fila y columna. Ej. 1 2" << std::endl;
        std::cin >> fila >> columna;
        std::cout << "> Coloca " << jugadorActual.getFicha() << " en fila " << fila << " y columna " << columna << std::endl;

        tablero.colocar(fila, columna, jugadorActual.getFicha());
        std::cout << tablero << std::endl;

        turno++;

        std::cout << '\n'
                  << std::string(30, '-') << std::endl;

        if (hayGanador() || hayEmpate())
        {
            seguir = false;
            if (hayGanador())
                std::cout << "> ¡Fin de la partida! Ha ganado " << jugadorActual.getNombre() << std::endl;
            else
                std::cout << "> ¡Fin de la partida! ¡EMPATE!" << std::endl;
        }
    }
}

bool Partida::hayGanador()
{
    return tablero.check3enRaya();
}

bool Partida::hayEmpate()
{
    return tablero.getColocadas() == 9;
}