def main():
    sundays = 0
    day = 2
    for year in range(1901, 2001):
        for month in range(1, 13):
            month_length = 31
            if month == 4 or month == 6 or month == 9 or month == 11:
                month_length = 30
            elif month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                month_length = 29
            elif month == 2:
                month_length = 28

            for i in range(month_length):
                if day % 7 == 0 and i == 0:
                    sundays += 1
                day += 1
    print(sundays)


if __name__ == "__main__":
    main()
