/* Person class */

#ifndef PERSON_H
#define PERSON_H

#include <string>

class Person {
	private:
		std::string name;
		int age;
		float height;
		float weight;

	public:
		Person(std::string name, int age, float height, float weight);
		~Person();
		void sayHello();
		int getAge();
};

#endif
