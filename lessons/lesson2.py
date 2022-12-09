import random

# Задание 1.
def sumDigitsInNumber():
    number = int(input('Введите вещественное число (десятичный разделитель - точка), чтобы узнать сумму цифр в нём: ').replace('.', ''))
    def sum(number):
        return 0 if number == 0 else int(number % 10) + sum(number // 10) 
    print(sum(number))

# Задание 2.
def listOfFuctorials():
    number = int(input('Введите число N, для получения массива факториалов от 0 до N: '))
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

# Задание 3.
def subsequentialSum():
    number = int(input('Введите число N, для вывода суммы от 0 до N последовательности (1 + 1/N)^N: '))
    sum = 0
    for i in range(1, number + 1):
        sum += (1 + 1/i)**i
    print(round(sum, 2))

# Задание 4.
def productOfElements():
    number = int(input('Введите число N, для вывода списка элементов от [-N; N]: '))
    numbers = []
    for i in range(-number, number + 1):
        numbers.append(i)
    print('Массив чисел: ', numbers)
    indexes = list(map(int, input('Введите индексы массива через пробел для вывода произведения значений по индексу: ').split(' ')))
    product = 1
    for i in indexes:
        product *= numbers[i]
    print(product)

# Задание 5.
def arrayShaffle():
    numbers = list(map(int, input('Введите элементы массива через пробел для перемешивания: ').split(' ')))
    shaffledNumbers = []
    while(len(numbers) > 0):
        value = random.choice(numbers)
        shaffledNumbers.append(value)
        numbers.remove(value)
    print(shaffledNumbers)

lessonTwo = [sumDigitsInNumber, listOfFuctorials, subsequentialSum, productOfElements, arrayShaffle]
