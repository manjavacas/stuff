#include <iostream>
#include <vector>

using namespace std;

/********************************************
 * Invierte el orden de un vector de enteros.
 ********************************************/
void invertor(vector<int> &vect)
{
    vector<int>::iterator it1 = vect.begin();
    vector<int>::iterator it2 = vect.end() - 1;

    int aux;

    while (it1 <= it2)
    {
        aux = *it1;
        *it1 = *it2;
        *it2 = aux;

        it1++;
        it2--;
    }
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