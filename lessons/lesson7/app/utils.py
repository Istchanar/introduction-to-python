import os
import datetime
import app.config as config


def logger(data: str):
    time = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(config.logPath, 'a+') as logs:
        logs.write(f'{time} {data};\n')


def deleteFile(path):
    try:
        os.remove(path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def printHelp():
    print('\u001b[36m' + 'For select the following actions, type number of command. Type "exit" for complite.')
    print('1. Get a list of contacts;\n'
          '2. Get a contact by data;\n'
          '3. Add a contact;\n'
          '4. Delete a contact;\n'
          '5. Export contacts;\n'
          '6. Help;\n'
          '7. Remove logs;\n'
          '8. Remove all contacts.\n')
