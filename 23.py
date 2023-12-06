import math
import multiprocessing

def abundant_number(number):
    if not number % 2 == 0 and not number % 3 == 0:
        return
    if number < 945 and number % 2 == 1:
        return
    sum = 0
    for i in range(1, math.ceil(math.sqrt(number))):
        if number % i == 0:
            sum += number
            if i != number / i and i != 1:
                sum += number / i

    return sum > number

def main():
    pool = multiprocessing.Pool(12)

    non_abundant_sums = pool.map(abundant_sum, range(1, 28123))

    total = 0
    for non_abundant_sum in non_abundant_sums:
        if non_abundant_sum is int:
            total += non_abundant_sum
    print(total)

def abundant_sum(number):
    print(number)
    abundant = False
    for i in range(1, number):
        if(abundant_number(i) and abundant_number(number - i)):
            abundant = True
    if not abundant:
        return number

                

if __name__ == "__main__":
    main()
