#include <iostream>
#include <queue>
#include <vector>

using namespace std;

/**************************************************************
 * Alumno/a:
 * Grupo:
 **************************************************************/

/**************************************************************
 Combina dos colas ordenadas (colaA, colaB) en una unica cola
 tambien ordenada (el minimo valor se encuentra en el frente).
**************************************************************/
queue<int> combinar_ordenadas(queue<int> colaA, queue<int> colaB)
{
    queue<int> colaC;

    // COMPLETAR
    // ...

    return colaC;
}

int main()
{
    // NO MODIFICAR

    vector<int> numsA = {1, 2, 2, 3, 3, 4, 5, 5};
    vector<int> numsB = {1, 2, 3, 3, 8, 9};

    queue<int> colaA;
    queue<int> colaB;
    queue<int> colaC;

    // Leer y mostrar cola A
    cout << "Cola A: ";
    for (int n : numsA)
    {
        colaA.push(n);
        cout << n << " ";
    }
    cout << endl;

    // Leer y mostrar cola B
    cout << "Cola B: ";
    for (int n : numsB)
    {
        colaB.push(n);
        cout << n << " ";
    }
    cout << endl;

    // Combinar colas ordenadas
    colaC = combinar_ordenadas(colaA, colaB);

    // Mostrar cola combinada
    cout << "\nCola combinada: ";
    while (!colaC.empty())
    {
        cout << colaC.front() << " ";
        colaC.pop();
    }
    cout << endl;

    return 0;
}