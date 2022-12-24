import functools
import random


def sum_of_the_digits():
    numbers = int(input('Input real number(decimal separator - dot), for output sum if the digits: ').replace('.', ''))
    sum_numbers = functools.reduce(lambda x, y: x + y, [int(number) for number in numbers]) 
    print(sum_numbers)


def list_of_fuctorials():
    number = int(input('Enter a number N, for generate array of factorials from 0 to N: '))
    fuctorials = []

    def fuctorial(n):
        if n == 0:
            fuctorials.append(1)
            return 1
        value = n * fuctorial(n - 1)
        fuctorials.append(value)
        return value
    fuctorial(number)
    print(fuctorials)


def sum_subsequential():
    number = int(input('Enter a number N, for return from 0 to N sum (1 + 1/N)^N subsequential: '))
    sum = 0
    for i in range(1, number + 1):
        sum += (1 + 1/i)**i
    print(round(sum, 2))


def product_of_elements():
    number = int(input('Enter the size of the array: '))
    numbers = [i for i in range(-number, number + 1)]
    print('Generated array: ', numbers)
    indexes = list(map(int, input('Enter array indexes to display products, separated by space: ').split(' ')))
    product = 1
    for i in indexes:
        product *= numbers[i]
    print(product)


def array_shaffle():
    numbers = list(map(int, input('Enter array elements (separated by space) to shuffle: ').split(' ')))
    shaffled_numbers = []
    while (len(numbers) > 0):
        value = random.choice(numbers)
        shaffled_numbers.append(value)
        numbers.remove(value)
    print(shaffled_numbers)


exercise_2 = [sum_of_the_digits, list_of_fuctorials, sum_subsequential, product_of_elements, array_shaffle]
