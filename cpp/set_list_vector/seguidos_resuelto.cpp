#include <iostream>
#include <vector>
#include <set>

using namespace std;

/***********************************************
 * Devuelve true si todo set Ci+1 es una
 * continuacion de Ci.
/**********************************************/
bool seguidos(vector<set<int>> vect)
{
    vector<int> nums;

    for (auto cjto : vect)
        for (int x : cjto)
            nums.push_back(x);

    for (int i = 1; i < nums.size(); i++)
        if (nums[i] != nums[i - 1] + 1)
            return false;

    return true;
}

int main()
{
    // NO MODIFICAR

    vector<set<int>> vectorA = {{1, 2, 3}, {4, 5}, {6}};
    vector<set<int>> vectorB = {{1, 2}, {3, 5}, {4, 6}};

    if (seguidos(vectorA))
        cout << "Vector A: true" << endl;
    if (seguidos(vectorB))
        cout << "Vector B: true" << endl;

    return 0;
}