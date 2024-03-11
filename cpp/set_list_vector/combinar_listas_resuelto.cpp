#include <iostream>
#include <list>

using namespace std;

/**************************************************************
 * Introduce la lista ordenada listaB en la
 * lista ordenada listaA, preservando el orden.
 **************************************************************/

/***************************** VERSION 1 ******************************/

void combinar_listas(list<int> &listaA, const list<int> listaB)
{
    list<int>::iterator itA = listaA.begin();

    for (list<int>::const_iterator itB = listaB.begin(); itB != listaB.end(); itB++)
    {
        while (*itA < *itB && itA != listaA.end())
            itA++;

        listaA.insert(itA, *itB);
    }
}

/******************** VERSION 2 (utilizando auto) ********************/

void combinar_listas_v2(list<int> &listaA, const list<int> listaB)
{
    auto itA = listaA.begin();

    for (auto itB = listaB.begin(); itB != listaB.end(); itB++)
    {
        while (itA != listaA.end() && *itA < *itB)
            itA++;

        listaA.insert(itA, *itB);
    }
}

/******************* VERSION 3 (utilizando for-each) ******************/

void combinar_listas_v3(list<int> &listaA, const list<int> listaB)
{
    auto itA = listaA.begin();

    for (int elemB : listaB)
    {
        while (itA != listaA.end() && *itA < elemB)
            itA++;

        listaA.insert(itA, elemB);
    }
}

int main()
{
    list<int> listaA = {0, 1, 1, 3, 4, 5, 6, 7};
    list<int> listaB = {0, 2, 4, 8, 9};

    combinar_listas(listaA, listaB);
    // combinar_listas_v2(listaA, listaB);
    // combinar_listas_v3(listaA, listaB);

    cout << "Listas combinadas: \n";
    for (int n : listaA)
        cout << n << " ";
    cout << endl;

    return 0;
}