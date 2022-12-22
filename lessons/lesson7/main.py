import ui_actions as ui

new_app = ui.window_configurate(ui.app, 'Telephone directory', 245, 400)

def new_app_start():
    ui.component_button(new_app, ui.get_all_contacts_dialog, '1. Get all contacts', 25, 2, '#c489c3', 1, 0)
    ui.component_button(new_app, ui.get_contact_dialog, '2. Find contacts', 25, 2, '#c489c3', 1, 1)
    ui.component_button(new_app, ui.set_contact_dialog, '3. Add contact in database', 25, 2, '#c489c3', 2, 0)
    ui.component_button(new_app, ui.delete_contact_dialog, '4. Delete contact from database', 25, 2, '#c489c3', 2, 1)
    ui.component_button(new_app, ui.export_contacts_dialog, '5. Export contacts in file', 25, 2, '#c489c3', 3, 0)
    ui.component_button(new_app, ui.help_dialog, '6. Help information', 25, 2, '#c489c3', 3, 1)
    ui.component_button(new_app, ui.remove_logs_dialog, '7. Remove logs file', 25, 2, '#c489c3', 4, 0)
    ui.component_button(new_app, ui.remove_all_data_dialog, '8. Remove all contacts', 25, 2, '#c489c3', 4, 1)
    new_app.mainloop()

new_app_start()