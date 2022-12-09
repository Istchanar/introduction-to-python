import random

def createRundomArray(size: int, minValue: int, maxValue: int) -> list:
    numbers = [i for i in range(random.randint(1, size))]
    return list(map(lambda value: random.randint(minValue, maxValue), numbers))

# Задание 1.
def sumOddIndexes():
    print('Программно задаётся массив, сумма значений на нечётных индексах равна: ')
    numbers = createRundomArray(10, -10, 10)
    print('Сгенерированный массив: ', numbers)
    oddSum = 0
    for i in range(0, len(numbers)):
        if(i%2 != 0):
            oddSum += numbers[i]
    print(oddSum)

# Задание 2.
def sumOfPairs():
    print('Программно задаётся массив, возвращается массив сум пар элементов (первого и последнего, второго и предпоследнего и т.д.): ')
    numbers = createRundomArray(10, -10, 10)
    print('Сгенерированный массив: ', numbers)
    sumOfPairs = []
    i, j = 0, len(numbers) - 1
    while(i <= j):
        sumOfPairs.append(numbers[i] + numbers[j])
        i, j = i + 1, j - 1
    print(sumOfPairs)


# Задание 3.
def maxNumberAfterPoint():
    print('Программно задаётся массив вещественных чисел, возвращается разница между max и min значением дробной части: ')
    numbers = [i for i in range(random.randint(1, 10))]
    setNumbers = list(map(lambda value: round(random.random()*10, 2), numbers))
    print('Сгенерированный массив: ', setNumbers)
    fractionalParts = sorted(list(map(lambda value: round(value % 1, 2), setNumbers)))
    print('Числа после запятой:    ', fractionalParts)
    print(round(fractionalParts[-1] - fractionalParts[0], 2))

# Задание 4
def numberinBinarryForm():
    print(bin(int(input('Введите число N, для получения числа N в бинарном представлении: '))).replace("0b", ""))


# Задание 5
def fibonacciList():
    number = int(input('Введите число N, чтобы получить ряд Фибоначчи: '))
    def fibonacciNumber(n):
        if(n in {0, 1}):
            return n
        elif(n == -1):
            return 1
        elif(n > 0):
            return fibonacciNumber(n - 1) + fibonacciNumber(n - 2)
        else:
            return fibonacciNumber(n + 2) - fibonacciNumber(n + 1)

    print([fibonacciNumber(n) for n in range(number * -1 , number + 1)])

lessonThree = [sumOddIndexes, sumOfPairs, maxNumberAfterPoint, numberinBinarryForm, fibonacciList]
