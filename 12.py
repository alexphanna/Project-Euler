import math

def prime(number):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0 and number != i:
            return False
    return True

def lowest_factor(number):
    for i in range(2, int(number)):
        if number % i == 0:
            return i

def prime_factors(number):
    numbers = []
    factor = lowest_factor(number)
    while not prime(number):
        numbers.append(factor)
        number = number // factor
        if (not prime(number)):
            factor = lowest_factor(number)
        else:
            numbers.append(number)
    return numbers

def count_exponents(numbers):
    exponents = []
    i = 0
    count = 1
    while i < len(numbers):
        if (i < len(numbers) - 1 and numbers[i] == numbers[i + 1]):
            count += 1
        elif (i == len(numbers) - 1 and numbers[i] == numbers[i - 1]):
            exponents.append(count)
            count += 1
        else:
            exponents.append(count)
            count = 1
        i += 1
    return exponents

def divisors(exponents):
    sum = 1
    for i in exponents:
        sum *= i + 1
    return sum

def main():
    number = 1
    triangle_number = 1
    number_of_divisors = 0
    while (number_of_divisors <= 500):
        number_of_divisors = divisors(count_exponents(prime_factors(triangle_number)))
        print(number, " | ", triangle_number, " | ", number_of_divisors)
        number += 1
        triangle_number += number

if __name__ == '__main__':
    main()