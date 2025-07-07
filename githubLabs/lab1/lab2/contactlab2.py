
contacts = { }

def add_contact(contacts, phone, first_name,last_name):
    
    if phone  in contacts:
        return 'error, contact already in file'
    else:
        contacts[phone] = [first_name,last_name]
        return str(phone) + ' Added:' + first_name + ", " + last_name + ""

def modefy_contact(contacts, phone, firs_name,last_name):
    
    if not phone in contacts:
        return 'error'
    else:
        
        contacts[id] = [firs_name,last_name]
        return str(phone) + ':' + firs_name + last_name 
    
def delete_contact(contacts,phone):
    if not phone in contacts:
        print("Can not find contact")
    else:
        contacts.pop(phone)
        return contacts
    
def find_contact(contacts, find):
    
    d = { }
    
    if find.isdigit():
        f =  int(find)
        if f in contacts:
            d[f] = contacts[f]
    
    for key, value in contacts.items():
        if find.lower() in value[0].lower() or find.lower() in value[1].lower():
            d[key] = value
        
    return d
    
    
            