import datetime
import os
import config

def logger(data: str):
    time = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(config.logPath, 'a+') as logs:
        logs.write(f'{time} {data}\n')

def deleteLogFile():
    try:
        os.remove(config.logPath)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))