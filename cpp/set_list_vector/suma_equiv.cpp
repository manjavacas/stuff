#include <iostream>
#include <vector>
#include <set>

using namespace std;

/***********************************************
 * Devuelve true si existen al menos dos
 * conjuntos cuya suma de valores sea la misma.
/**********************************************/
bool suma_equiv(vector<set<int>> vect)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<set<int>> vectorA = {{1, 2, 3}, {4, 5}, {6}};
    vector<set<int>> vectorB = {{1, 2}, {3, 4}, {5, 6}};

    if (suma_equiv(vectorA))
        cout << "Vector A: true" << endl;
    if (suma_equiv(vectorB))
        cout << "Vector B: true" << endl;

    return 0;
}