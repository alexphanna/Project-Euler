def main():
    number = 0
    divisible = False
    while not divisible:
        number += 1
        divisible = True
        for i in range(1, 21):
            if number % i != 0:
                divisible = False
                break
    print(number)

if __name__ == '__main__':
    main()