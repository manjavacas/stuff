#include <iostream>
#include <queue>
#include <string>

void encolar(std::string num, std::queue<int> &colaNumeros);
void separar(std::queue<int> colaNumeros, std::queue<int> &colaPares, std::queue<int> &colaImpares);
void mostrar(std::string texto, std::queue<int> cola);

int main(int argc, char **argv)
{
    std::queue<int> colaNumeros;
    std::queue<int> colaPares;
    std::queue<int> colaImpares;

    if (argc == 2)
    {
        encolar(argv[1], colaNumeros);
        separar(colaNumeros, colaPares, colaImpares);
        mostrar("- Cola impares: ", colaImpares);
        mostrar("- Cola pares: ", colaPares);
    }
    else
        std::cout << "Usage: ./reverse <word>" << std::endl;

    return 0;
}

void encolar(std::string num, std::queue<int> &colaNumeros)
{
    for (char c : num)
        colaNumeros.push(c - '0');
}

void separar(std::queue<int> colaNumeros, std::queue<int> &colaPares, std::queue<int> &colaImpares)
{
    while (!colaNumeros.empty())
    {
        if (colaNumeros.front() % 2)
            colaImpares.push(colaNumeros.front());
        else
            colaPares.push(colaNumeros.front());
        colaNumeros.pop();
    }
}

void mostrar(std::string texto, std::queue<int> cola) {
    std::cout << texto << '\n';
    while(!cola.empty()) {
        std::cout << cola.front() << " ";
        cola.pop();
    }
    std::cout << "\n";
}