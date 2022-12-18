import datetime
import os
import config

def logger(data: str):
    time = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(config.logPath, 'a+') as logs:
        logs.write(f'{time} {data}\n')