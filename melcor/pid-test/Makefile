all: gen cor
gen: clean
	./MELGEN branch.inp
cor:
	./MELCOR ow=o i=branch.inp 
clean:
	rm -f *.PTF
	rm -f *.DIA
	rm -f *.MES
	rm -f *.OUT
	rm -f *.RST
	rm -f *.DAT
	rm -f MEGDIA
	rm -f MEGOUT
	rm -f MELDIA
	rm -f MELOUT
	rm -f MELMES
	rm -f MELPTF
	rm -f MELRST
	rm -f fort*
	rm -f extDIAG