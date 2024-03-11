#ifndef PARTIDA_H
#define PARTIDA_H

#include <string>

#include "Jugador.h"
#include "Tablero.h"

class Partida {
    private:
        Jugador jugador1;
        Jugador jugador2;
        Tablero tablero;
        bool partidaFinalizada();
        bool hayGanador();
        bool hayEmpate();
    public:
        Partida(std::string nombre1, std::string nombre2);
        void jugar();
};

#endif