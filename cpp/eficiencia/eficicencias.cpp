#include <iostream>
#include <ctime>
#include <cstdlib>

int buscar1(const int *v, const int n, const int x);
int buscar2(const int *v, const int n, const int x);
int buscar3(const int *v, const int n, const int x);
void ordenar(int *v, const int n);

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        std::cout << "Uso: " << argv[0] << " <n> <max_value>"
                  << std::endl;
        return 1;
    }

    int n = atoi(argv[1]);
    int max_value = atoi(argv[2]);
    // int x = max_value + 1;

    clock_t t_ini;
    clock_t t_fin;

    srand(time(0));

    int *v = new int[n];
    for (int i = 0; i < n; i++)
        v[i] = rand() % max_value;

    t_ini = clock();
    ordenar(v, n);
    t_fin = clock();

    std::cout << (t_fin - t_ini) / (double)CLOCKS_PER_SEC << std::endl;

    delete[] v;

    return 0;
}

int buscar1(const int *v, const int n, const int x)
{
    // T(n) = 1 + 4 + n(4 + 1 + 1) + 1 + 1 = 7 + 6n € O(n)
    int i = 0;
    while (i < n && v[i] != x)
        i++;
    if (i < n)
        return i;
    else
        return -1;
}

int buscar2(const int *v, const int n, const int x)
{
    // T(n) = 4 + n(4 + 2) + 1 = 5 + 6n € O(n)
    for (int i = 0; i < n; i++)
        if (v[i] == x)
            return i;
    return -1;
}

int buscar3(const int *v, const int n, const int x)
{
    // T(n) = 1 + 1 + n(1 + 2 + 2) + 1 = 3 + 5n € O(n)
    int i = 0;
    while (i < n)
    {
        if (v[i] == x)
            return i;
        i++;
    }
    return -1;
}

void ordenar(int *v, const int n)
{
    int aux;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (v[j] > v[j + 1])
            {
                aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
            }
}