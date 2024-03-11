#include <iostream>
#include <list>
#include <set>

using namespace std;

/**********************************************************
 * Ordena de menor a mayor tamaño una lista de conjuntos.
 *********************************************************/
void size_sort(list<set<int>> &lista)
{
    set<int> aux;

    for (auto it1 = lista.begin(); it1 != lista.end(); it1++)
        for (auto it2 = next(it1); it2 != lista.end(); it2++)
        {
            if (it1->size() > it2->size()) // similar a (*it).size()
            {
                aux = *it1;
                *it1 = *it2;
                *it2 = aux;
            }
        }
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