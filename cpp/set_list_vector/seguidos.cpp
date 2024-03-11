#include <iostream>
#include <vector>
#include <set>

using namespace std;

/***********************************************
 * Devuelve true si todo set Ci+1 es una
 * continuacion de Ci.
/**********************************************/
bool seguidos(vector<set<int>> vect)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<set<int>> vectorA = {{1, 2, 3}, {4, 5}, {6}};
    vector<set<int>> vectorB = {{1, 2}, {3, 5}, {4, 6}};

    if (seguidos(vectorA))
        cout << "Vector A: true" << endl;
    if (seguidos(vectorB))
        cout << "Vector B: true" << endl;

    return 0;
}