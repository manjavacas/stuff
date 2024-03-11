#!/bin/bash

N_MAX=30000
INC=500

V_MAX=10
i=100

while [ $i -lt $N_MAX ]
do
    ./a.out $i $V_MAX >> tiempos.dat
    i=$((i + $INC))
done
