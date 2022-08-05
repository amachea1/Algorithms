#1.Compute the sum of digits in all numbers from 1 to n.
from random import randint

dig_num = int(input('Enter how many digits are in number '))

def sum_digits(digits):
    if digits < 1:
        print(digits)
    down = 10 ** (digits - 1)
    up = 10 ** digits - 1
    n = randint(down, up)
    print(n)
    result = 0
    i = 0
    while i < digits:
        result += n % 10
        n = n // 10
        i += 1
    return result

print(sum_digits(dig_num))

#2. # Find max number from 3 values, entered manually from a keyboard

num1 = int(input('Enter 1st number '))
num2 = int(input('Enter 2nd number '))
num3 = int(input('Enter 3rd number '))

def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'Max number is 1st number {num1}')
    elif num2 > num1 and num2 > num3:
        print(f'Max number is 2nd number {num2}')
    elif num1 == num2:
        print(f'1st number {num1} is equal to 2nd number {num2}')
    elif num2 == num3:
        print(f'2nd number {num2} is equal to 3rd number {num3}')
    elif num1 == num3:
        print(f'1st number {num1} is equal to 3rd number {num3}')
    else:
        print(f'Max number is 3rd number {num3}')

max_number(num1, num2, num3)

#3.Count odd and even numbers.
n = int(input('Enter number '))

def count_odd_even(num):
    odd_count = 0
    even_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    print(f'There are {even_count} even digits in a number')
    print(f'There are {odd_count} odd digits in a number')

count_odd_even(n)