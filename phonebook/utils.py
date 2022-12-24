import os
import datetime

# Export text files path
exports_path = 'phonebook/exports/'
data_base_path = 'phonebook/data_base/data_base.csv'
logs_path = 'phonebook/logs/logs.txt'

# Pics path
icon_path = './phonebook/images/magenta_icon.png'

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
