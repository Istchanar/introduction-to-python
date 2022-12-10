import random
import tkinter as tk

# Задание 1.
def removeSubstring():
    print('Из файла data/lesson5/stringWithABC.txt удаляется подстрока "абв" и записывается в файл stringWithoutABC.txt: ')
    filePathFirst, filePathSecond = 'data/lesson5/stringWithABC.txt', 'data/lesson5/stringWithoutABC.txt'
    encodingParam = 'utf-8'
    with open(filePathFirst, 'r', encoding=encodingParam) as stringWithABC:
        stringFromFile = stringWithABC.read().replace('абв', '')
    with open(filePathSecond, 'w', encoding=encodingParam) as stringWithoutABC:
        stringWithoutABC.writelines(stringFromFile)
    print('Результат работы: ', stringFromFile)

# Задание 2.
def candyGame():
    candys = 2021
    print('Игра 2021 конфета, кто делает последний ход - заберает всё!')
    player = random.randint(1, 2)
    print(f'Первый ход Игрока #1, если выпало 1, или Игрока #2, если выпало 2. Выпало:', player)
    while(candys > 0):
        c = 0
        while( c < 1 or c > 29 or c > candys):
            c = int(input(f'Очередь Игрока #{player}, можно брать от 1 до 28 конфет: '))
        candys -=  c
        player = 2 if player == 1 else 1
        print('Осталось конфет:', candys)
    print(f'Поздравляю, выиграл Игрок #{2 if player == 1 else 1}!')

# Задание 3.
def ticTacToe():
    def printBoard(board: list):
        for row in board:
            for item in row:
                print(item, end = ' ')
            print()
    
    def checkWiner(player: str, board: list) -> bool:
        if (board[0][0] == board[0][1] == board[0][2] == player): return True
        if (board[1][0] == board[1][1] == board[1][2] == player): return True
        if (board[2][0] == board[2][1] == board[2][2] == player): return True
        if (board[0][0] == board[1][0] == board[2][0] == player): return True
        if (board[0][1] == board[1][1] == board[2][1] == player): return True
        if (board[0][2] == board[1][2] == board[2][2] == player): return True
        if (board[0][0] == board[1][1] == board[2][2] == player): return True
        if (board[0][2] == board[1][1] == board[2][0] == player): return True
        return False

    player = 'X' if random.randint(1, 2) == 1 else 'O'
    gameBoard = [['-' for j in range(3)] for i in range(3)]
    print(f'Игра крестики-нолики! Первым ходит игрок, играющий за {player} (случайный выбор): ')

    while(True):
        printBoard(gameBoard)
        print()
        row, column = list(map(int, input(f'Введите номер колонки и строки для записи {player}: ').split()))
        gameBoard[row - 1][column - 1] = player
        print()
        if(checkWiner(player, gameBoard)): 
            print(f"Игрок {player} победил!")
            break
        player = 'X' if player == 'O' else 'O'
    
    printBoard(gameBoard)

# Задание 4.
def implementationOfRLE():
    # Test data: AduuBBBCCCCCCcccccCCCCCCCCCAfffffffx
    def encodeRLE() -> str:
        stringData = text.get()
        text.delete(0, tk.END)
        stringLength = len(stringData)
        encodeString = ''
        numberOfChars = 1
        for i in range(1, stringLength):
            if(stringData[i - 1] == stringData[i]): numberOfChars += 1
            else:
                encodeString += f'{numberOfChars}' + stringData[i - 1]
                numberOfChars = 1
            if(i + 1 == stringLength): encodeString += f'{numberOfChars}' + stringData[i]
        text.insert(0, encodeString)

    def decodeRLE() -> str:
        encodeString = text.get()
        text.delete(0, tk.END)
        countOfChars = [int(number) for number in encodeString[0::2]]
        chars = [char for char in encodeString[1::2]]
        decodeString = ''
        for i in range(0, len(chars)):
            decodeString += ''.join(chars[i] for j in range(countOfChars[i]))
        text.insert(0, decodeString)
    
    app = tk.Tk()
    app.geometry('400x110')
    app.title('RLE decode')
    text = tk.Entry(app, font=('Calibri 12'))
    encodeButton = tk.Button(app, text='encode', command=encodeRLE, width=25, height=2)
    decodeButton = tk.Button(app, text='decode', command=decodeRLE, width=25, height=2)
    text.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=10)
    encodeButton.grid(row=2, column=0, padx=5, pady=5)
    decodeButton.grid(row=2, column=1, padx=5, pady=5)
    app.mainloop()

lessonFive = [removeSubstring, candyGame, ticTacToe, implementationOfRLE]