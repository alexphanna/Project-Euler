def divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def main():
    total = 0
    for i in range(10000):
        if i == sum(divisors(sum(divisors(i)))) and i != sum(divisors(i)):
            print(i, ",", sum(divisors(i)), ",", sum(divisors(sum(divisors(i)))))
            total += i
    print(total)


if __name__ == "__main__":
    main()