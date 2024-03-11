#include "snake.h"

#define INITIAL_LENGTH 3;

Snake::Snake()
{
    length = INITIAL_LENGTH;
    body = new snakepart[length];

    for (int i = 0; i < length; i++)
    {
        snakepart part;
        part.x = i + 3;
        part.y = 0;
        body[i] = part;
    }
}

void Snake::move(int dir_x, int dir_y) {
    // TO-DO
    // de la snakepart 1 a la ultima, (x, y) = (x, y) de la que esta delante
    // sumar dir_x y dir_y a la primera snakepart
}

void Snake::grow() {
    // TO-DO
    // incrementar en 1 el tamaño del vector body
    // añadir elemento al final
}