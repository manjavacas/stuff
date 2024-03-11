#ifndef SNAKE_H
#define SNAKE_H

struct snakepart {
    int x;
    int y;
};

class Snake {
    private:
        int length;
        snakepart* body;
    public:
        Snake();
        int getLength();
        void move(int dir_x, int dir_y);
        void grow();
};

#endif