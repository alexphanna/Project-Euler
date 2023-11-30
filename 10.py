import math

def prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    sum = 0
    for i in range(2, 2000000):
        if prime(i):
            sum += i
    print(sum)

if __name__ == '__main__':
    main()