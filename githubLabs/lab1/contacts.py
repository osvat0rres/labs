import json

class Contacts:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = {}

        try:
            with open(self.filename, "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            pass
        
    def add_contact(self, id, first_name, last_name):
        if id in self.contacts:
            return "Contact with ID {} already exists.".format(id)

        self.contacts[id] = [first_name, last_name]

        self._sort_contacts()

        with open(self.filename, "w") as f:
            json.dump(self.contacts, f)

        return id

    def modify_contact(self, id, first_name, last_name):
        if id not in self.contacts:
            return "Contact with ID {} does not exist.".format(id)

        self.contacts[id] = [first_name, last_name]

        self._sort_contacts()

        with open(self.filename, "w") as f:
            json.dump(self.contacts, f)

        return id

    def delete_contact(self, id):
        if id not in self.contacts:
            return "Contact with ID {} does not exist.".format(id)

        contact = self.contacts.pop(id)

        with open(self.filename, "w") as f:
            json.dump(self.contacts, f)

        return contact

    def print_contacts(self):
        print("Last Name\t\tFirst Name\t\tPhone")
        for last_name, contact in self.contacts.items():
            first_name, phone = contact
            print("{}\t\t{}\t\t{}".format(last_name, first_name, phone))

    def set_filename(self, filename):
        self.filename = filename

    def _sort_contacts(self):
        self.contacts = sorted(self.contacts.items(), key=lambda x: (x[0].lower(), x[1][0].lower()))