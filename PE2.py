def main():
    a, b, sum = 1, 2, 0
    while a <= 4000000:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
    return sum

if __name__ == "__main__":
    print(main())


# This program calculates the sum of even Fibonacci numbers not exceeding four million.