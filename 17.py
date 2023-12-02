TENTHS = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
HUNDREDTHS = [ "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]

def number_to_word(number):
    word = ""
    if number == 1000:
        word += "one thousand"
    else:
        if number > 99:
            word += TENTHS[number % 1000 // 100 - 1] + " hundred"
            if number % 100 != 0:
                word += " and "
        if number % 100 > 19:
            word += HUNDREDTHS[number % 100 // 10 - 1]
            if number % 10 != 0:
                word += "-"
        if number % 10 != 0 and (number % 100 // 10 != 1):
            word += TENTHS[number % 10 - 1]
        elif number % 100 // 10 == 1:
            word += TENTHS[number % 100 - 1]

    return word

def main():
    total = ""
    for i in range(1, 1001):
        total += number_to_word(i)
    total = total.replace(" ", "")
    total = total.replace("-", "")
    print(len(total))

if __name__ == "__main__":
    main()