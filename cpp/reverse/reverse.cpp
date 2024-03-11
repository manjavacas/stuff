#include <iostream>
#include <stack>
#include <string>

std::string reverse(std::string word)
{
    std::stack<char> stack;

    for (char c : word)
        stack.push(c);

    for (int i = 0; !stack.empty(); ++i)
    {
        word[i] = stack.top();
        stack.pop();
    }
    
    return word;
}

int main(int argc, char **argv)
{
    if (argc == 2)
        std::cout << reverse(argv[1]) << std::endl;
    else
        std::cout << "Usage: ./reverse <word>" << std::endl;

    return 0;
}