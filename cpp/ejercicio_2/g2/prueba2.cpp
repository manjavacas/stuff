#include <iostream>
#include <vector>
#include <set>

/*********************************************
 * Alumno/a: 
 * Grupo: 
*********************************************/

using namespace std;

/*********************************************
 * Devuelve TRUE si todo numero entre 0 y n-1
 * esta incluido en el vector cjtos.
*********************************************/
bool incluidos(int n, vector<set<int>> cjtos)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<set<int>> cjtos = {{0, 2, 3, 4}, {0, 1, 3, 4}, {1, 2, 5, 6}, {2, 3, 4, 5}};

    string resultadoA = incluidos(7, cjtos) ? "true" : "false";
    string resultadoB = incluidos(8, cjtos) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;

    return 0;
}