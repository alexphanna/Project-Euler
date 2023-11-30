def fibonacci(first, second, max):
    sequence = [first, second]
    while (first + second < max):
        temp = first
        first = second
        second += temp
        sequence.append(second)
    return sequence

def main():
    sequence = fibonacci(1, 2, 4000000)
    sum = 0
    for number in sequence:
        if number % 2 == 0:
            sum += number
    print(sum)

if __name__ == '__main__':
    main()