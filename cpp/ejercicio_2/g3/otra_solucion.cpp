#include <iostream>
#include <list>
#include <set>

/*********************************************
 * Alumno/a: ANTONIO MANJAVACAS
 * Grupo: A1,A2,A3
 *********************************************/

using namespace std;

/*********************************************
 * Devuelve TRUE si los conjuntos en lista
 * son subconjuntos propios consecutivos.
 *********************************************/
bool proper_subset(list<set<int>> lista)
{
    auto it = lista.begin();

    while (it != prev(lista.end()))
    {
        set<int> actual = *it;
        set<int> siguiente = *next(it);

        for (int n : actual)
            if (siguiente.find(n) == siguiente.end())
                return false;
        it++;
    }
    return true;
}

int main()
{
    // NO MODIFICAR

    list<set<int>> listaA = {{1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4, 6}};
    list<set<int>> listaB = {{1, 2, 3}, {1, 2, 3, 4}, {1, 3, 4, 6}};

    string resultadoA = proper_subset(listaA) ? "true" : "false";
    string resultadoB = proper_subset(listaB) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;
}