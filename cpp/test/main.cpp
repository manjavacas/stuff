#include "Person.h"
#include <iostream>

int main() {
	Person p("John", 20, 1.59, 64.1);
	p.sayHello();
	
	std::cout << "Mi age is: " << p.getAge() << std::endl;
	
	return 0;
}
