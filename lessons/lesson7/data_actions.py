import csv
import utils


def get_contact(find_string: str, contacts: list) -> list:
    filtered_contacts = list(filter(lambda row: find_string in row, contacts))
    utils.logger(f'With data: {find_string} get_one_contact_data() call successfully')
    return filtered_contacts


def get_all_contacts() -> list:
    with open(utils.data_base_path, 'r', newline='') as csv_data:
        all_contacts = list(map(lambda row: row, csv.reader(csv_data, delimiter=',', quotechar='|')))
    utils.logger(f'Data received successfully, get_all_contacts() call')
    return all_contacts


def set_contact(new_contact: list):
    with open(utils.data_base_path, 'a+', newline='') as csv_data:
        csv.writer(csv_data, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow(new_contact)
    utils.logger(f'Add data into a database, addPhonesData() call, query data: {new_contact}')


def delete_contact(find_string: str) -> list:
    contacts = get_all_contacts()
    filter_contacts = list(
        filter(lambda contact: find_string not in contact, contacts))
    deleted_contacts = list(
        filter(lambda contact: find_string in contact, contacts))
    utils.delete_file(utils.data_base_path)
    with open(utils.data_base_path, 'w', newline='') as csv_data:
        csv.writer(csv_data, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerows(filter_contacts)
    utils.logger(f'Entry deleted, deletePhoneInData() call, query data: {find_string}')
    return deleted_contacts


def delete_all_contacts():
    utils.delete_file(utils.data_base_path)
    with open(utils.data_base_path, 'w', newline='') as csv_data:
        csv.writer(csv_data, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL).writerow(utils.headers)
    utils.logger('All contacts deleted, deletePhonesDataAll() call')
