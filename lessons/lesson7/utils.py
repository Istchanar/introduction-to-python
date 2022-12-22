import os
import datetime

# Export text files path
exports_path = 'lessons/lesson7/exports/'
data_base_path = 'lessons/lesson7/data_base/data_base.csv'
logs_path = 'lessons/lesson7/logs/logs.txt'

# Pics path
icon_path = './lessons/lesson7/images/magenta_icon.png'

# Data headers
headers = ['Name', 'Surname', 'Address', 'Phone number']

# Logger
def logger(data: str):
    time = datetime.datetime.now().strftime('%m.%d.%Y %H:%M:%S')
    with open(logs_path, 'a+') as logs:
        logs.write(f'{time} {data};\n')

# Delete file
def delete_file(path: str):
    try:
        os.remove(path)
        logger(f'File {path} deleted successfully')
    except OSError as e:
        logger('ERROR: %s - %s.' % (e.filename, e.strerror))
