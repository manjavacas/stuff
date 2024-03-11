#include <iostream>
#include <list>
#include <set>

using namespace std;

/**********************************************************
 * Ordena de menor a mayor tamaño una lista de conjuntos.
 *********************************************************/
void size_sort(list<set<int>> &lista)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    list<set<int>> lista = {{3, 4, 5}, {0}, {1, 2}, {6, 7, 8, 9}};

    size_sort(lista);

    cout << "Lista ordenada: \n";
    for (set<int> cjto : lista)
    {
        cout << "{ ";
        for (int num : cjto)
            cout << num << " ";
        cout << "} ";
    }
    cout << endl;

    return 0;
}