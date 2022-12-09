import math
import random
import sympy

# Задание 1.
def fixedPointPi():
    print(round(math.pi, len(input('Введите число в формате (например 0.01) для вывода числа pi с заданной точностью: ')) - 2))

# Задание 2.
def numberFactorization():
    number = input('Введите число для получения массива простых множителей числа: ')
    primeNumbers = set()
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            primeNumbers.add(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1: primeNumbers.add(number)
    print(primeNumbers)

# Задание 3.
def uniqueValues():
    randomList = [random.randint(1, 10) for i in range(0, 10)]
    print('Генерируется массив размера 10 со значениями (1, 10) для вывода уникальных чисел:\n', randomList)
    print('Уникальные числа в массиве:', [number for number in randomList if(randomList.count(number) < 2)])

# Задание 4.
def polynomialInFile():
    filePath = 'data/polynomialString.txt'
    power = int(input('Введите степень для генерации и записи в файл data/polynomialString.txt многочлена (с коэффициенами от 1 до 100): '))
    polynomial = ""
    while(power >= 0):
        number = random.randint(0, 100)
        if(number == 0):
            power -= 1
            continue
        if(power > 1): 
            polynomial += f'{number}*x**{power} + '
        elif (power == 1):
            polynomial += f'{number}*x + '
        elif (power == 0): 
            polynomial += f'{number} = 0' 
        power -= 1
    with open(filePath, 'w') as polynomialFile:
        polynomialFile.write(polynomial)

# Задание 5.
def polynomialSumFromFile():
    print('Результат суммирования двух многочленов из файлов data/polynomial1.txt, data/polynomial2.txt: ')
    filePathFirst, filePathSecond, polynomialSum = 'data/polynomial1.txt', 'data/polynomial2.txt', 'data/polynomialSum.txt'
    with open(filePathFirst, 'r') as polynomial1:
        stringOne = polynomial1.read().split('=')[0]
    with open(filePathSecond, 'r') as polynomial1:
        stringTwo = polynomial1.read().split('=')[0]
    with open(polynomialSum, 'w') as polynomial:
        polynomial.writelines(f'{str(sympy.powsimp(stringOne + "+" + stringTwo))} = 0')

lessonFour = [fixedPointPi, numberFactorization, uniqueValues, polynomialInFile, polynomialSumFromFile]
