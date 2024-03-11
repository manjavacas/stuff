#include <iostream>
#include <vector>

using namespace std;

/********************************************
 * Invierte el orden de un vector de enteros.
 ********************************************/
void invertor(vector<int> &vect)
{
    // COMPLETAR
    // ...
}

int main()
{
    // NO MODIFICAR

    vector<int> vect = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    invertor(vect);

    cout << "Vector invertido: \n";
    for (int n : vect)
        cout << n << " ";
    cout << endl;

    return 0;
}