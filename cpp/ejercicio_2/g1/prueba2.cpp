#include <iostream>
#include <vector>
#include <set>

/************************************************
 * Alumno/a:
 * Grupo:
 ************************************************/

using namespace std;

/************************************************
 * Devuelve TRUE si existe al menos un elemento
 * que pertenece a todos los conjuntos en cjtos.
 ************************************************/
bool en_todos(vector<set<int>> cjtos)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<set<int>> vectorA = {{0, 2, 3, 4, 5}, {0, 1, 5, 7}, {2, 3, 5, 6, 7}};
    vector<set<int>> vectorB = {{0, 2, 3, 4, 5}, {0, 1, 7}, {2, 3, 5, 6, 7}};

    string resultadoA = en_todos(vectorA) ? "true" : "false";
    string resultadoB = en_todos(vectorB) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;

    return 0;
}