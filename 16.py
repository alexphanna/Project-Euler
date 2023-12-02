def digit(number, digit):
    return int((number % 10**(digit + 1)) / 10**(digit))

def digits(number):
    len = 1
    while number > 9:
        number = number // 10
        len += 1
    return len

def main():
    number = 2**1000
    sum = 0
    for i in range(digits(number)):
        sum += digit(number, i)
    print(sum)

if __name__ == "__main__":
    main()