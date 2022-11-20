import math
import sys

# Задание 1.
def dayCheck():
    dict = {'1':'Нет', '2':'Нет', '3':'Нет', '4':'Нет', '5':'Нет', '6':'Да', '7':'Да'} 
    number = input('Задание 1. Введите цифру дня недели для проверки, выходной ли это: ')
    print('Такого дня недели не существует.' if not (number in dict) else dict.get(number))

#Задание 2.
def predicatCheck():
    print('Вывод значений всех предикатов по формуле not(X or Y or Z) == not(X) and not(Y) and not(Z): ')
    for i in 0, 1:
        for j in 0, 1:
            for k in 0, 1:
                print(i, j, k, '-',(not (i or j or k)) == ((not i) and (not j) and (not k)))
# Задание 3.
def coordinateQuarter():
    point = list(map(int, input('Введите через проблел координаты двух точек, для вывода четверти: ').split(' ')))
    if(point[0] == 0 or point[1] == 0): return print('Одна из координат равна 0.')
    print('I четверть.' if point[1] > 0 else 'IV четверть.') if point[0] > 0 else print('III четверть.' if point[1] < 0 else 'II четвертеть.')

# Задание 4.
def coordinateRange():
    x = int(input('Введите номер четверти для отображения диапазона возможных координат точки: '))
    print(f'[ 0 < x < {math.inf if (x == 1 or x == 4) else -math.inf}, 0 < y < {math.inf if x == 1 or x == 2 else -math.inf}]')

# Задание 5.
def distance2D():
    print('Введите через проблел координаты двух точек, для расчёта расстояния в 2D пространстве: ')
    pointA = list(map(float, input('Координаты точки A: ').split(' ')))
    pointB = list(map(float, input('Координаты точки B: ').split(' ')))
    print(math.sqrt(round((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2, 2)))

while(True):
    try:
        value = input('Урок первый, введите номер задания, для выхода введите exit: ')
        match value:
            case '1':
                dayCheck()
            case '2':
                predicatCheck()
            case '3':
                coordinateQuarter()
            case '4':
                coordinateRange()
            case '5':
                distance2D()
            case 'exit':
                break
    except:
        print('При выполнении программы возника ошибка (неправильные данные и т.д.)')

sys.exit()