#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool incluidos(int n, vector<set<int>> cjtos)
{
    for (int i = 0; i < n; i++)
    {
        int count = 0;
        for (auto cjto : cjtos)
            if (cjto.find(i) != cjto.end())
                count++;
        if (!count)
            return false;
    }

    return true;
}

int main()
{
    vector<set<int>> cjtos = {{0, 2, 3, 4}, {0, 1, 3, 4}, {1, 2, 5, 6}, {2, 3, 4, 5}};

    string resultadoA = incluidos(7, cjtos) ? "true" : "false";
    string resultadoB = incluidos(8, cjtos) ? "true" : "false";

    cout << "Caso 1: " << resultadoA << endl;
    cout << "Caso 2: " << resultadoB << endl;

    return 0;
}