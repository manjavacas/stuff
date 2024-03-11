#ifndef SCREEN_H
#define SCREEN_H

#include <iostream>

class Screen
{
private:
    int height;
    int width;
    int **board;

public:
    Screen(int height, int width);
    int getHeight();
    int getWidth();
    int getValueAt(int x, int y);
    void setValueAt(int x, int y, int value);
};

std::ostream &operator<<(std::ostream &outstream, Screen screen);

#endif