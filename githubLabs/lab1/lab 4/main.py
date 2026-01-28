from contacts import*


if __name__ == "__main__":
    contacts = Contacts()

    menu_options = {
        "1": "Add contact",
        "2": "Modify contact",
        "3": "Delete contact",
        "4": "Print contact list",
        "5": "Set contact filename",
        "6": "Exit the program"
    }

    while True:
        print("Tuffy Titan Contact List")
        for key, option in menu_options.items():
            print("{}. {}".format(key, option))

        menu_choice = input("Enter menu choice: ")

        if menu_choice not in menu_options:
            print("Invalid menu choice.")
            continue

        if menu_choice == "6":
            break

        if menu_choice == "1":
            id = input("Enter ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            result = contacts.add_contact(id, first_name, last_name)
            if result != id:
                print(result)
        elif menu_choice == "2":
            id = input("Enter ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            result = contacts.modify_contact(id, first_name, last_name)
            if result != id:
                print(result)
        elif menu_choice == "3":
            id = input("Enter ID: ")

            result = contacts.delete_contact(id)
            if result is None:
                print("Contact deleted successfully.")
            else:
                print(result)
        elif menu_choice == "4":
            contacts.print_contacts()
        elif menu_choice == "5":
            filename = input("Enter contact filename: ")
            contacts.set_filename(filename)