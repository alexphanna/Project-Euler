def main():
    f = open("names.txt", "r")
    names = f.readline().replace("\"", "")[:-1].split(",")
    names.sort()
    total = 0
    for i in range(len(names)):
        sum = 0
        for j in names[i]:
            sum += ord(j) - 64
        sum *= i + 1
        total += sum
        print(names[i], sum)
    print(total)

if __name__ == "__main__":
    main()