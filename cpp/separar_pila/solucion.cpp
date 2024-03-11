#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

void separar(stack<int> &pila, int medio)
{
    stack<int> pila_min;
    stack<int> pila_max;

    while (!pila.empty())
    {
        if (pila.top() > medio)
            pila_max.push(pila.top());
        else if (pila.top() < medio)
            pila_min.push(pila.top());
        pila.pop();
    }

    while (!pila_min.empty())
    {
        pila.push(pila_min.top());
        pila_min.pop();
    }

    pila.push(medio);

    while (!pila_max.empty())
    {
        pila.push(pila_max.top());
        pila_max.pop();
    }
}

int main(int argc, char **argv)
{

    // Rellenar pila con valores

    vector<int> nums = {1, 17, 12, 15, 10, 0, 2, 4, 8, 24, 6};
    stack<int> pila;

    int medio = 10;

    for (int n : nums)
        pila.push(n);

    // Separar

    separar(pila, medio);

    // Mostrar resultado

    cout << "Pila separada por valor medio = " << medio << '\n';
    while (!pila.empty())
    {
        cout << pila.top() << " ";
        pila.pop();
    }
    cout << endl;

    return 0;
}