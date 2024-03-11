#include <iostream>
#include <string>

#include "Partida.h"

int main()
{

    std::string nombre1;
    std::string nombre2;

    bool repetir = true;

    std::cout << "¡Bienvenido!" << std::endl;

    while (repetir)
    {
        std::cout << "> Introducir nombre del jugador 1 (O): " << std::endl;
        std::cin >> nombre1;

        std::cout << "> Introducir nombre del jugador 2 (X): " << std::endl;
        std::cin >> nombre2;

        Partida partida(nombre1, nombre2);

        partida.jugar();

        std::cout << "> ¿Nueva partida? (0 = No, 1 = Si)" << std::endl;
        std::cin >> repetir;
    }

    std::cout << "> ¡Hasta la vista!" << std::endl;

    return 0;
}