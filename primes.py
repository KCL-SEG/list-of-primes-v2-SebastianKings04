"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError
    else:
        list = []
        count = 0 
        i = 2
        while count < number_of_primes:
            if isPrime(i):
                list.append(i)
                count += 1
            i += 1
        return list

def isPrime(number):
    if number not in (2,3,5,7):
        if not(number % 2):
            return False
        elif not(number % 3):
            return False
        elif not(number % 5):
            return False 
        elif not(number % 7):
            return False
        else:
            return True
    else:
            return True
