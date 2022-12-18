import sys


def main():
    while(True):
        try:
            print('\u001b[35m' + '\nTelephone directory.\n')
            print( '\u001b[36m' + '1. Get a list of contacts;\n'\
            '2. Add a contact;\n'\
            '3. Delete a contact\n'\
            '4. Export contacts\n'\
            '5. Remove logs\n')
            actionChoise = input('\033[32m' + 'Select the following actions (number of command, type "exit" for complite): ' + '\033[0m')
            if (actionChoise == 'exit'): break
        except:
            print('Unexpected error (reading a file, entering data, etc)')
    sys.exit()

main()