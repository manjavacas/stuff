#include "screen.h"
#include "snake.h"

#include <iostream>

int main()
{
    Screen screen(20, 20);
    Snake snake();

    std::cout << screen << std::endl;
    return 0;
}