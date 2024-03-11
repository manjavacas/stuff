#include "Person.h"
#include <iostream>

Person::Person(std::string name, int age, float height, float width) {
	this->name = name;
	this->age = age;
	this->height = height;
	this->weight = weight;
}

Person::~Person() {}

void Person::sayHello() {
	std::cout << "Hello! I'm " << name << std::endl;
}

int Person::getAge() {
	return this->age;
}
