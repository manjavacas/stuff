#include "screen.h"
#include <cassert>

#define MIN_WIDTH 10
#define MAX_WIDTH 10

Screen::Screen(int height, int width) : height(height), width(width)
{
    assert(width > 10 && height > 10);

    board = new int *[height];
    for (int x = 0; x < height; x++)
    {
        board[x] = new int[width];
        for (int y = 0; y < width; y++)
        {
            board[x][y] = 0;
        }
    }
}

int Screen::getHeight()
{
    return height;
}

int Screen::getWidth()
{
    return width;
}

int Screen::getValueAt(int x, int y)
{
    return board[x][y];
}

void Screen::setValueAt(int x, int y, int value)
{
    board[x][y] = value;
}

std::ostream &operator<<(std::ostream &outstream, Screen screen)
{
    char c;
    for (int x = 0; x < screen.getHeight(); x++)
    {
        for (int y = 0; y < screen.getWidth(); y++)
        {
            switch (screen.getValueAt(x, y))
            {
            case 0:
                c = ' ';
                break;
            case 1:
                c = 'S';
                break;
            case 2:
                c = 'F';
                break;
            }
            outstream << c;
        }
        outstream << std::endl;
    }
    return outstream;
}