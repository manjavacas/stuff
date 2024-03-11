#include <iostream>
#include <set>
#include <list>
#include <vector>

using namespace std;


int main()
{
    vector<int> vect = {1,2,3,4,5};

    vector<int>::iterator it = vect.begin();

    while(it != vect.end()) {
        if(*it % 2) {
            it = vect.erase(it);
        } else {
            it++;
        }
    }



    return 0;
}