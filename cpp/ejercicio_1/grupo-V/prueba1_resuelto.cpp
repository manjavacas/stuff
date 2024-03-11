#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/**************************************************************
 * Alumno/a: ANTONIO MANJAVACAS
 * Grupo: -
 **************************************************************/

/**************************************************************
 Combina dos pilas ordenadas (pilaA, pilaB) en una unica pila
 tambien ordenada (el minimo valor se encuentra en la cima).
**************************************************************/
stack<int> combinar_ordenadas(stack<int> pilaA, stack<int> pilaB)
{
    stack<int> pilaC;

    while (!pilaA.empty() && !pilaB.empty())
    {
        if (pilaA.top() <= pilaB.top())
        {
            pilaC.push(pilaB.top());
            pilaB.pop();
        }
        else
        {
            pilaC.push(pilaA.top());
            pilaA.pop();
        }
    }

    while (!pilaA.empty())
    {
        pilaC.push(pilaA.top());
        pilaA.pop();
    }

    while (!pilaB.empty())
    {
        pilaC.push(pilaB.top());
        pilaB.pop();
    }

    return pilaC;
}

int main()
{
    // NO MODIFICAR

    vector<int> numsA = {1, 2, 2, 3, 3, 4, 5, 5};
    vector<int> numsB = {1, 2, 3, 3, 8, 9};

    stack<int> pilaA;
    stack<int> pilaB;
    stack<int> pilaC;

    // Leer y mostrar pila A
    cout << "Pila A: ";
    for (int n : numsA)
    {
        pilaA.push(n);
        cout << n << " ";
    }
    cout << endl;

    // Leer y mostrar pila B
    cout << "Pila B: ";
    for (int n : numsB)
    {
        pilaB.push(n);
        cout << n << " ";
    }
    cout << endl;

    // Combinar pilas ordenadas
    pilaC = combinar_ordenadas(pilaA, pilaB);

    // Mostrar pila combinada
    cout << "\nPila combinada: ";
    while (!pilaC.empty())
    {
        cout << pilaC.top() << " ";
        pilaC.pop();
    }
    cout << endl;

    return 0;
}