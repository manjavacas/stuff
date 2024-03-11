run: gen cor
gen: clean
	./melgen-fusion-186_bdba SAMPLE.inp
cor:
	./melcor-fusion-186_bdba ow=o i=SAMPLE.inp 
control:
	./control.py
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