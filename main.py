import sys
from lessons.lesson1 import lessonOne
from lessons.lesson2 import lessonTwo
from lessons.lesson3 import lessonThree
from lessons.lesson4 import lessonFour
from lessons.lesson5 import lessonFive
from lessons.lesson6 import lessonSix

def main():
    lessons = [lessonOne, lessonTwo, lessonThree, lessonFour, lessonFive, lessonSix]
    while(True):
        try:
            lessonNumber = input('\033[32m' + 'Введите номер урока (exit для выхода): ' + '\033[0m')
            if (lessonNumber == 'exit'): break
            exerciseNumber = input('\033[35m' + f'Урок {lessonNumber}, введите номер задания (exit для выхода): ' + '\033[0m')
            if (exerciseNumber == 'exit'): break
            lessons[int(lessonNumber) - 1][int(exerciseNumber) - 1]()

        except:
            print('При выполнении программы возника ошибка (неправильные данные, номер урока и т.д.)')
    sys.exit()

if __name__ == "__main__":
    main()