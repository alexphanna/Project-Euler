import math

def palindromic(number):
    for i in range(0, math.ceil(digits(number) / 2)):
        if digit(number, i) != digit(number, digits(number) - i - 1 + digits(number) % 2):
            return False
    return True

def digit(number, digit):
    return int((number % 10**(digit + 1)) / 10**(digit))

def digits(number):
    len = 0
    while number > 9:
        number /= 10
        len += 1
    return len

def main():
    highest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if palindromic(i * j) and i * j > highest_palindrome:
                highest_palindrome = (i * j)
    print(highest_palindrome)

if __name__ == '__main__':
    main()
