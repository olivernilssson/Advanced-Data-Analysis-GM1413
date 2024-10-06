# Exercise 1.2: Sum of Digits

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n = n // 10
    print(sum_digits)


sum_of_digits(int(input('Enter a positive integer: ')))
