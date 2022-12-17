import functools
import random

# Задание 3.
def maxNumberAfterPoint():
    print('Программно задаётся массив вещественных чисел, возвращается разница между max и min значением дробной части: ')
    numbers = [i for i in range(random.randint(1, 10))]
    setNumbers = list(map(lambda value: round(random.random()*10, 2), numbers))
    print('Сгенерированный массив: ', setNumbers)
    fractionalParts = sorted(list(map(lambda value: round(value % 1, 2), setNumbers)))
    print('Числа после запятой:    ', fractionalParts)
    print(round(fractionalParts[-1] - fractionalParts[0], 2))

# Задание 3.
def uniqueValues():
    randomList = [random.randint(1, 10) for i in range(0, 10)]
    print('Генерируется массив размера 10 со значениями (1, 10) для вывода уникальных чисел:\n', randomList)
    print('Уникальные числа в массиве:', [number for number in randomList if(randomList.count(number) < 2)])

# Задание 1.
def sumDigitsInNumber():
    numbers = input('Введите вещественное число (десятичный разделитель - точка), чтобы узнать сумму цифр в нём: ').replace('.', '')
    sumNumbers = functools.reduce(lambda x, y: x + y, [int(number) for number in numbers]) 
    print(sumNumbers)

def createRundomArray(size: int, minValue: int, maxValue: int) -> list:
    numbers = [i for i in range(random.randint(1, size))]
    return list(map(lambda value: random.randint(minValue, maxValue), numbers))

# Задание 1.
def sumOddIndexes():
    print('Программно задаётся массив, сумма значений на нечётных индексах равна: ')
    numbers = createRundomArray(10, -10, 10)
    print('Сгенерированный массив: ', numbers)
    oddSum = 0
    for i, number in enumerate(numbers):
        if(i%2 != 0):
            oddSum += number
    print(oddSum)

lessonSix = [maxNumberAfterPoint, uniqueValues, sumDigitsInNumber, sumOddIndexes]