import random
import tkinter as tk


def remove_substring():
    print('Substrings "abc" are removed from "/text_data/string_includes_abc.txt" and write in "/text_data/string_excludes_abc.txt:" ')
    path_first, path_second = 'exercises/text_data/string_includes_abc.txt', 'exercises/text_data/string_excludes_abc.txt'
    with open(path_first, 'r', encoding='utf-8') as string_includes_abc:
        clean_string = string_includes_abc.read().replace('abc', '')
    with open(path_second, 'w', encoding='utf-8') as string_excludes_abc:
        string_excludes_abc.writelines(clean_string)
    print('Result: ', clean_string)


def candy_game():
    candys = 2021
    print('Candy game, whoever makes the last move takes everything!')
    player = random.randint(1, 2)
    print(f'First turn of player #1, if a 1 is rolled, or player #2, if a 2. Rolled:', player)
    while (candys > 0):
        c = 0
        while (c < 1 or c > 29 or c > candys):
            c = int(
                input(f'Your turn #{player}, you can pick up from 1 to 28 candies: '))
        candys -= c
        player = 2 if player == 1 else 1
        print('Total candys', candys)
    print(f'Player #{2 if player == 1 else 1} win!')


def tic_tac_toe():
    def print_board(board: list):
        for row in board:
            map(lambda cell: print(cell, end=' '), row)
            print()

    def check_winner(player: str, board: list) -> bool:
        if (board[0][0] == board[0][1] == board[0][2] == player):
            return True
        if (board[1][0] == board[1][1] == board[1][2] == player):
            return True
        if (board[2][0] == board[2][1] == board[2][2] == player):
            return True
        if (board[0][0] == board[1][0] == board[2][0] == player):
            return True
        if (board[0][1] == board[1][1] == board[2][1] == player):
            return True
        if (board[0][2] == board[1][2] == board[2][2] == player):
            return True
        if (board[0][0] == board[1][1] == board[2][2] == player):
            return True
        if (board[0][2] == board[1][1] == board[2][0] == player):
            return True
        return False

    player = 'X' if random.randint(1, 2) == 1 else 'O'
    board = [['-' for i in range(3)] for j in range(3)]
    print(
        f'Tic tac toe! The player playing for {player} goes first (random choice): ')
    while (True):
        print_board(board)
        print()
        row, column = list(map(int, input(
            f'Enter the column and row number for the entry {player}: ').split()))
        board[row - 1][column - 1] = player
        print()
        if (check_winner(player, board)):
            print(f"Player {player} win!")
            break
        player = 'X' if player == 'O' else 'O'
    print_board(board)


def implementation_of_RLE_ui():
    def encode_RLE() -> str:
        data = text.get()
        text.delete(0, tk.END)
        data_length = len(data)
        encoded_string = ''
        count_of_chars = 1
        for i in range(1, data_length):
            if (data[i - 1] == data[i]):
                count_of_chars += 1
            else:
                encoded_string += f'{count_of_chars}' + data[i - 1]
                count_of_chars = 1
            if (i + 1 == data_length):
                encoded_string += f'{count_of_chars}' + data[i]
        text.insert(0, encoded_string)

    def decode_RLE() -> str:
        data = text.get()
        text.delete(0, tk.END)
        count_of_chars = [int(number) for number in data[0::2]]
        chars = [char for char in data[1::2]]
        decoded_string = ''
        for i in range(0, len(chars)):
            decoded_string += ''.join(chars[i]
                                      for j in range(count_of_chars[i]))
        text.insert(0, decoded_string)

    window = tk.Tk()
    window.geometry('400x110')
    window.title('RLE decode')
    text = tk.Entry(window, font=('Calibri 12'))
    encodeButton = tk.Button(window, text='encode',
                             command=encode_RLE, width=25, height=2)
    decodeButton = tk.Button(window, text='decode',
                             command=decode_RLE, width=25, height=2)
    text.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=10)
    encodeButton.grid(row=2, column=0, padx=5, pady=5)
    decodeButton.grid(row=2, column=1, padx=5, pady=5)
    window.mainloop()


exercise_5 = [remove_substring, candy_game, tic_tac_toe, implementation_of_RLE_ui]
