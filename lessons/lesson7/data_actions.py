import csv
import config

def getPhonesData():
    with open(config.dataPath, 'r', newline='') as csvData:
       data = csv.reader(csvData, delimiter=',', quotechar='|')
       print(type(data))
       return data
        

def printPhonesData(data):
    headers = next(data)
    print('Headers: ', headers)
    for row in data:
        print(', '.join(row))

printPhonesData(getPhonesData())