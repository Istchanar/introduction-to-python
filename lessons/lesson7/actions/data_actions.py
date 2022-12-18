import csv
import utils
from lessons.lesson7.config import *

def getPhonesData():
    with open(dataPath, 'r', newline='') as csvData:
        dataStream = csv.reader(csvData, delimiter=',', quotechar='|')
        headers = next(dataStream)
        print('Headers: ', headers)
        data = list(map(lambda x: ' '.join(x), dataStream))
        return data

def printPhonesData(data: list):
        list(map(lambda x:print(x), data))

def deletePhonesDataAll(path: str):
        utils.deleteFile(path)
        with open(path) as csvData:
                csvData = csv.writer(path, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                csvData.writerow(headers)

deletePhonesDataAll()