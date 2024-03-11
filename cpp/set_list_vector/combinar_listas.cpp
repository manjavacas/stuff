#include <iostream>
#include <list>

using namespace std;

/**************************************************************
 * Introduce la lista ordenada listaB en la 
 * lista ordenada listaA, preservando el orden.
**************************************************************/
void combinar_listas(list<int> &listaA, const list<int> listaB)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    list<int> listaA = {0, 1, 1, 3, 4, 5, 6, 7};
    list<int> listaB = {0, 2, 4, 8, 9};

    combinar_listas(listaA, listaB);

    cout << "Listas combinadas: \n";
    for (int n : listaA)
        cout << n << " ";
    cout << endl;

    return 0;
}