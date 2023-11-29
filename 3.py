import math 

def prime(number):
    for i in range(2, math.ceil(math.sqrt(number))):
        if number % i == 0:
            return False
    return True

def lowest_factor(number):
    for i in range(2, int(number)):
        if number % i == 0:
            return i

def prime_factorization(number):
    factor = lowest_factor(number)
    while not prime(number):
        number /= factor
        if (not prime(number)):
            factor = lowest_factor(number)
    return number

def main():
    print(prime_factorization(600851475143))

if __name__ == '__main__':
    main()
