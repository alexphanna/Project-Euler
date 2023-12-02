def main():
    max_count = 0
    max_number = 0
    for i in range(1000000):
        count = 1
        number = i
        while number > 1:
            if number % 2 == 0:
                number /= 2
            elif number % 2 == 1:
                number = number * 3 + 1
            count += 1
        if count > max_count:
            max_count = count
            max_number = i
    print(max_number)

if __name__ == "__main__":
    main()