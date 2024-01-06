def main():
    index = 1
    while digits(fibonacci(index)) != 1000:
        index += 1
    print(index)

def fibonacci(index, memo={}):
    if index in memo:
        return memo[index]
    elif index == 1 or index == 2:
        result = 1
    else:
        result = fibonacci(index - 1, memo) + fibonacci(index - 2, memo)
    memo[index] = result
    return result

def digits(number):
    return len(str(number))
  
if __name__ == "__main__":
    main()