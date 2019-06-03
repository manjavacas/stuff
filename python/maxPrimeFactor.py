'''
Created on 19 ene. 2019
@author: Antonio Manjavacas
Largest prime factor of N
'''

N = 600851475143


def MaxPrimeFactor(n):
    factor = 2
    lastFactor = 1
    
    while n > 1:
        if n % factor == 0:
            lastFactor = factor
            n //= factor
            
            # Exponents greater than 1
            while n % factor == 0:
                n //= factor
        factor += 1
    return lastFactor


print("Maximum prime factor of " + str(N) + " = " + str(MaxPrimeFactor(N)))
