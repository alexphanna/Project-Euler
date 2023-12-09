import math
import multiprocessing

divisors = []
def abundant_number(number):
    return divisors[number - 1] > number

def main():
    for i in range(1, 28123 + 1):
        sum = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                sum += j
                if i / j != j and j != 1:
                    sum += i / j
        divisors.append(sum)

    pool = multiprocessing.Pool(12)

    non_abundant_sums = pool.map(abundant_sum, range(1, 28123 + 1))

    total = 0
    for non_abundant_sum in non_abundant_sums:
        if not non_abundant_sum is None:
            total += non_abundant_sum
    print(total)

def abundant_sum(number):
    for i in range(1, number):
        if(abundant_number(i) and abundant_number(number - i)):
            return None
    return number

                

if __name__ == "__main__":
    main()
