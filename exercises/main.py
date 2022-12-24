import sys
from exercise1 import exercise_1
from exercise2 import exercise_2
from exercise3 import exercise_3
from exercise4 import exercise_4
from exercise5 import exercise_5


def main():
    groups = [exercise_1, exercise_2, exercise_3, exercise_4, exercise_5]
    colors = {'Reset': '\033[0m', 'Purple': '\033[35m', 'Green': '\033[32m'}
    exit_command = 'exit'
    while(True):
        try:
            group_number = input(colors['Green'] + f'Select group of exercises (type "{exit_command}" for close): ' + colors['Reset'])
            if (group_number == exit_command): break
            exercise_number = input(colors['Purple'] + f'Group {group_number}, type number of exercise (type "{exit_command}" for close): ' + colors['Reset'])
            if (exercise_number == exit_command): break
            groups[int(group_number) - 1][int(exercise_number) - 1]()
        except:
            print('Something went wrong (invalid exercise number, data, etc.)')
    sys.exit()


if __name__ == "__main__":
    main()