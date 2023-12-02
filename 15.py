def factorial(number):
    if number == 1:
        return number
    return factorial(number - 1) * number

def combinations(objects, sample):
    return factorial(objects) / (factorial(sample) * factorial(objects - sample))

def main():
    print(combinations(40, 20))

if __name__ == "__main__":
    main()