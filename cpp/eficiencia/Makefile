all: clean compile run
clean:
	rm -f ./a.out
compile:
	g++ *.cpp
run:
	./a.out 10000 100
test: clean compile
	rm -f tiempos.dat
	sh test.sh
