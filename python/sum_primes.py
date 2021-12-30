
def primesBelow(givenNumber):  
    
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break       
        if isPrime:
            primes.append(possiblePrime)
    
    return(primes)

print(sum(primesBelow(2000000)))
