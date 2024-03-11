#include <iostream>
#include <list>
#include <set>

using namespace std;

/*************************************************
 * Elimina todos los sets cuya suma sea igual a n 
/************************************************/
void limpiar_suma(list<set<int>> &lista, int n)
{
    list<set<int>> limpia;

    for (set<int> cjto : lista)
    {
        int sum = 0;
        for (int i : cjto)
            sum += i;
        if (sum != n)
            limpia.push_back(cjto);
    }

    lista = limpia;
}

int main()
{
    // NO MODIFICAR

    list<set<int>> lista = {{1, 2}, {1, 4}, {5}, {3, 7}, {2, 3}};

    cout << "Original:  ";
    for (auto cjto : lista)
    {
        cout << "{ ";
        for (int n : cjto)
            cout << n << " ";
        cout << "} ";
    }
    cout << endl;

    limpiar_suma(lista, 5);

    cout << "Resultado: ";
    for (auto cjto : lista)
    {
        cout << "{ ";
        for (int n : cjto)
            cout << n << " ";
        cout << "} ";
    }
    cout << endl;

    return 0;
}