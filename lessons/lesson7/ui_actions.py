import tkinter as tk
import data_actions
import export_actions
import utils

app = tk.Tk()


def window_configurate(window: tk.Tk, title: str, window_height: int, window_width: int): 
    photo = tk.PhotoImage(file = utils.icon_path)
    window.wm_iconphoto(False, photo)
    window.title(title)
    screen_width = window.winfo_screenwidth()
    screen_heigth = window.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_heigth / 2) - (window_height / 2)
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, int(x), int(y)))
    return  window

    
def component_button(component: tk.Tk, function, text: str, weidth: int, height: int, color: str, row: int, column: int):
    custom_button = tk.Button(component, text = text, command = function, width = weidth, height = height, bg=color)
    custom_button.grid(row = row, column = column, padx = 7, pady=10)
    return custom_button


def component_input(component: tk.Tk, width: int):
    custom_input = tk.Entry(component, font = 'Helvetica  13', width = width, bg = '#d1c2d1')
    custom_input.grid(row = 1, column = 1, padx = 7, pady=20)
    return custom_input


def component_label(component: tk.Tk, text: str, x: int, y:  int):
    custom_label = tk.Label(component, text = text, font = 'Helvetica  10', justify='left')
    custom_label.place( x = x, y = y)
    return custom_label 


def create_labels(component: tk.Tk, data: list, distance_x: int, distance_y: int, shift: int, ljust: int):
    y = distance_y
    for text in data:
        tk.Label(component, text = ' '.join(text.ljust(ljust) for text in text), font = 'Helvetica  10').place( x = distance_x, y = y)
        y += shift


def get_all_contacts_dialog():
    data = data_actions.get_all_contacts()
    window = tk.Toplevel(app)
    window_configurate(window, 'Contacts', 200, 420)
    create_labels(window, data, 30, 10, 20, 17)


def get_contact_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Find contacts', 200, 365)
    input = component_input(window, 20)
    def press():
        contact = data_actions.get_contact(input.get(), data_actions.get_all_contacts())
        create_labels(window, contact, 25, 60, 20, 12)
        button['state'] = 'disabled'
        input.delete(0, tk.END)
    button = component_button(window, press, 'Search', 20, 1, '#c489c3', 1, 2)


def set_contact_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Set contact', 150, 490)
    input = component_input(window, 34)
    label = component_label(window, 'Click the Button for set contact.\nFormat:"Name,Surname,City,PhoneNumber"', 110, 60)
    def press():
        data_actions.set_contact(input.get().split(','))
        label['text'] = 'Data seted'
        label.place( x = 190, y = 60)
        button['state'] = 'disabled'
        input.delete(0, tk.END)
    button = component_button(window, press, 'Set', 20, 1, '#c489c3', 1, 2)


def delete_contact_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Delete contact', 200, 355)
    input = component_input(window, 19)
    label = component_label(window, 'Click the Button for delete contact.', 75, 110)

    def press():
        data = data_actions.delete_contact(input.get())
        label.place( x = 20, y = 60)
        label['text'] = 'Data deleted: '
        create_labels(window, data, 20, 80, 20, 13)
        button['state'] = 'disabled'
        input.delete(0, tk.END)
    button = component_button(window, press, 'Delete', 20, 1, '#c489c3', 1, 2)


def export_contacts_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Export contacts', 180, 430)
    label = component_label(window, 'Click the Button for export contacts.', 210, 70)
    def press_TXT():
        export_actions.export_TXT()
        label['text'] = f'Contacts successfully saved \nin ./exports/data_TXT.txt'
        button_TXT['state'] = 'disabled'
    button_TXT = component_button(window, press_TXT, 'Export in .txt', 25, 2, '#89b2c4', 1, 0)
    
    def press_PDF():
        export_actions.export_PDF()
        label['text'] = f'Contacts successfully saved \nin ./exports/data_PDF.pdf'
        button_PDF['state'] = 'disabled'
    button_PDF = component_button(window, press_PDF, 'Export in .pdf', 25, 2, '#bf7a91', 2, 0)
    
    def press_HTML():
        export_actions.export_HTML()
        label['text'] = f'Contacts successfully saved \nin ./exports/data_HTML.html'
        button_HTML['state'] = 'disabled'
    button_HTML = component_button(window, press_HTML, 'Export in .html', 25, 2, '#7abf97', 3, 0)


def help_dialog():
    text = '- You can change default file directories in utils.py;\n'\
           '- Support exports in PDF, TXT, HTML;\n'\
           '- Default exports path: ./root/exports/;\n'\
           '- Default log file path: ./root/logs/;\n'\
           '- Image folder (icons, etc.) in ./root/images;\n'\
           '- Data stored in csv format.'
    window = tk.Toplevel(app)
    window_configurate(window, 'Help info', 200, 400)
    component_label(window, text, 50, 30)


def remove_logs_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Logs file deleted', 150, 270)
    component_label(window, 'Logs file deleted.', 90, 50)
    utils.delete_file(utils.logs_path)
    button = component_button(window, window.destroy, 'Close', 20, 1, '#69b56d', 0, 0)
    button.place(x = 65, y = 110)


def remove_all_data_dialog():
    window = tk.Toplevel(app)
    window_configurate(window, 'Delete all contacts', 150, 270)
    component_label(window, 'Are you sure?', 90, 50)
    def press():
        utils.delete_file(utils.data_base_path)
        window.destroy()
    button_yes = component_button(window, press, 'Yes', 15, 1, '#bf6e5c', 0, 0)
    button_yes.place(x = 10, y = 110)
    button_no = component_button(window, window.destroy, 'No', 15, 1, '#69b56d', 0, 0)
    button_no.place(x = 143, y = 110)