#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool en_todos(vector<set<int>> cjtos)
{
    set<int> numeros;

    for (set<int> cjto : cjtos)
        for (int n : cjto)
            numeros.insert(n);

    for (int n : numeros)
    {
        int count = 0;
        for (set<int> cjto : cjtos)
            if (cjto.find(n) != cjto.end())
                count++;
        if (count == cjtos.size())
            return true;
    }
    return false;
}

int main()
{
    vector<set<int>> vectorA = {{0, 2, 3, 4, 5}, {0, 1, 5, 7}, {2, 3, 5, 6, 7}};
    vector<set<int>> vectorB = {{0, 2, 3, 4, 5}, {0, 1, 7}, {2, 3, 5, 6, 7}};

    string resultadoA = en_todos(vectorA) ? "true" : "false";
    string resultadoB = en_todos(vectorB) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;

    return 0;
}