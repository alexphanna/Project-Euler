import math

def pythagorean_triplet(a, b):
    return hypotenuse(a, b) % 1 == 0
    
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    for i in range(1, 1000):
        for j in range(i, 1000):
            if (pythagorean_triplet(i, j) and i + j + hypotenuse(i, j) == 1000):
                print(i * j * hypotenuse(i, j))
                

if __name__ == '__main__':
    main()