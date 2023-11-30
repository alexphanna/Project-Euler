import math

def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    number = 2
    for i in range(10001):
        while not prime(number):
            number += 1
        print(number)
        number += 1

if __name__ == '__main__':
    main()