#include <iostream>
#include <queue>
#include <vector>

using namespace std;

queue<int> intercalar(queue<int> colaA, queue<int> colaB)
{
    queue<int> colaC;

    while(!colaA.empty() && !colaB.empty()) {
        if(!colaA.empty()) {
            colaC.push(colaA.front());
            colaA.pop();
        }
        if(!colaB.empty()) {
            colaC.push(colaB.front());
            colaB.pop();
        }
    }

    while(!colaA.empty()) {
        colaC.push(colaA.front());
        colaA.pop();
    }

    while(!colaB.empty()) {
        colaC.push(colaB.front());
        colaB.pop();
    }

    return colaC;
}

int main()
{
    // NO MODIFICAR

    vector<int> numsA = {1, 3, 5, 7, 9};
    vector<int> numsB = {2, 4, 6, 8};

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
    colaC = intercalar(colaA, colaB);

    // Mostrar cola combinada
    cout << "\nCola con valores intercalados: ";
    while (!colaC.empty())
    {
        cout << colaC.front() << " ";
        colaC.pop();
    }
    cout << endl;

    return 0;
}