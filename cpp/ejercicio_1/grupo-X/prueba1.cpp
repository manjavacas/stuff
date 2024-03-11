#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/***********************************************************
 * Alumno/a:
 * Grupo:
 ***********************************************************/

/***********************************************************
 Reordena los elementos de una pila de tal manera que los 
 pares quedan por encima de los impares.
***********************************************************/
void flota_pares(stack<int> &pila)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<int> nums = {4, 9, 7, 2, 0, 17};
    stack<int> pila;

    // Leer y mostrar pila original
    cout << "Pila original: ";
    for (int n : nums)
    {
        pila.push(n);
        cout << n << " ";
    }

    // Reordenar elementos
    flota_pares(pila);

    // Mostrar pila reordenada
    cout << "\nPila reordenada: ";
    while (!pila.empty())
    {
        cout << pila.top() << " ";
        pila.pop();
    }
    cout << endl;

    return 0;
}