#include <iostream>
#include <list>
#include <set>

using namespace std;

bool proper_subset(list<set<int>> lista)
{
    while (lista.size() > 1)
    {
        set<int> c0 = lista.front();
        lista.pop_front();

        set<int> c1 = lista.front();

        for (int n : c0)
            if (c1.find(n) == c1.end())
                return false;
    }
    return true;
}

int main()
{
    list<set<int>> listaA = {{1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4, 6}};
    list<set<int>> listaB = {{1, 2, 3}, {1, 2, 3, 4}, {1, 3, 4, 6}};

    string resultadoA = proper_subset(listaA) ? "true" : "false";
    string resultadoB = proper_subset(listaB) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;
}