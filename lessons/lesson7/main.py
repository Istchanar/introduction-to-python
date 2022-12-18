import sys
import app.utils as utils
import app.config as config
import app.data_actions as action
import app.export_actions as export


def main():
    print('\u001b[35m' + '\nTelephone directory.\n')
    utils.printHelp()
    while (True):
        try:
            actionChoise = input('\033[32m' + 'Select the actions: ' + '\033[0m')
            if (actionChoise == 'exit'): break
            actions(int(actionChoise))
        except:
            print('Unexpected error (reading a file, entering data, etc)')
    sys.exit()


def actions(actionNumber: int):
    match actionNumber:
        case 1:
            print('\nContacts: ')
            action.printPhonesData(action.getPhonesDataAll())
        case 2:
            findContact = input('\nEnter data to search for contacts: ')
            action.printPhonesData(action.getPhoneData(
                findContact, action.getPhonesDataAll()))
        case 3:
            newContact = input(
                '\nEnter data to add a new contact (delimiter ","): ').split(",")
            action.setPhoneInData(newContact)
        case 4:
            deleteContact = input('\nEnter data to delete a contact: ')
            action.deletePhoneInData(deleteContact)
        case 5:
            fileType = input(
                '\nEnter file type (TXT, PDF, HTML) for create export file: ')
            export.switchExportType(fileType, action.getPhonesDataAll())
        case 6:
            utils.printHelp()
        case 7:
            print('\nLogs deleted.')
            utils.deleteFile(config.logPath)
        case 8:
            choise = input('\nAre you sure (type "yes" to delete)?: ')
            if (choise == 'yes'):
                action.deletePhonesDataAll()
        case _:
            print('Unexpected command.')
    print('')


main()
