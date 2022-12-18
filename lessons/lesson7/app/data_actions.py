import csv
import app.utils as utils
import app.config as config


def getPhonesDataAll() -> list:
    with open(config.dataPath, 'r', newline='') as csvData:
        data = list(map(lambda rowInData: rowInData, csv.reader(csvData, delimiter=',', quotechar='|')))
    utils.logger('Data received successfully, getPhonesData() call')
    return data


def getPhoneData(findString: str, contacts: list) -> list:
    filterData = list(filter(lambda contactData: findString in contactData, contacts))
    utils.logger('getPhoneData() call successfully')
    return filterData


def setPhoneInData(newData: list):
    with open(config.dataPath, 'a+', newline='') as csvData:
        csv.writer(csvData, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow(data)
    utils.logger(f'Add data into a database, addPhonesData() call, query data: {newData}')


def deletePhonesDataAll():
    utils.deleteFile(config.dataPath)
    with open(config.dataPath, 'w', newline='') as csvData:
        csv.writer(csvData, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow(config.headers)
    utils.logger('All data deleted, deletePhonesDataAll() call')


def deletePhoneInData(findString: str):
    filterData = list(filter(lambda contactData: findString not in contactData, getPhonesDataAll()))
    utils.deleteFile(config.dataPath)
    with open(config.dataPath, 'w', newline='') as csvData:
        csv.writer(csvData, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerows(filterData)
    utils.logger(f'Deleted entry, deletePhoneInData() call, query string: {findString}')


def printPhonesData(data: list):
    if (len(data) == 0): return print('Data empty/not exist.')
    list(map(lambda row: print(' '.join(text.ljust(17) for text in row)), data))
