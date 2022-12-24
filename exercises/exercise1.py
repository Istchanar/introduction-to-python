import math


def day_check():
    week = {'0': 'Yes', '1': 'No', '2': 'No', '3': 'No', '4': 'No', '5': 'No', '6': 'Yes'}
    num = input('Input day number of a week, and check if day a weekend: ')
    print('The number of the day does not exist.' if not (num in week) else week.get(num))
    

def predicates_print():
    print('Print all predicates: not X or Y or Z = not X and not Y and not Z: ')
    for i in 0, 1:
        for j in 0, 1:
            for k in 0, 1:
                print(i, j, k, '-', (not (i or j or k)) == ((not i) and (not j) and (not k)))


def coordinate_quarter():
    point = list(map(int, input('You enter the coordinates of two points separated by space for output quadrant: ').split(' ')))
    if (0 in point): return print('Coordinate contains zero.')
    if (point[0] > 0):
        print('First quandrant.' if point[1] > 0 else 'Fourth quandrant.')
    else:
        print('Third quandrant.' if point[1] < 0 else 'Second quandrant.')


def coordinate_quarter_range():
    num = int(input('Input number of quadrant for print available coordinate range: '))
    print(f'[ 0 < x < {math.inf if  num in (3, 4) else -math.inf}, 0 < y < {math.inf if  num in (1, 2) else -math.inf}]')


def two_point_distance():
    print('Enter in the x, y coordinates of the points for print the distance between: ')
    pointA = list(map(float, input('Point A coordinates: ').split(' ')))
    pointB = list(map(float, input('Point B coordinates: ').split(' ')))
    answer = math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2)
    print(round(answer, 2))


exercise_1 = [day_check, predicates_print, coordinate_quarter, coordinate_quarter_range, two_point_distance]
