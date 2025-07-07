
from contactlab2 import*

def manu():
    print("1. Add contact")
    print("2. Modefy contact")
    print("3. delete contact")
    print("4. print contact")
    print("5. Find contact")
    print("6. Exit program")
    
    option = input("Enter an option: ")
    
    return option

if __name__ == '__main__':
    
    all_contacts = { }
    while True:
        option = manu()
        
        if option == '1':
            
            phone = int(input("Enter the phone number: "))
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            
            print(add_contact(all_contacts,phone,first_name,last_name))
            
        elif option == '2':
            phone = int(input("Enter existimg phone number: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            
            print(modefy_contact(all_contacts, phone, first_name, last_name))
        elif option == '3':
            
            phone = int(input("Eneter the phone you want to delete: "))
            
            print(delete_contact(all_contacts,phone))
            
        elif option == '4':
            
            print("============= CONTACT LIST ============")
            print(f'{"Phone":<8}{'First':<8}{'Last':<8}')
            for key, value  in all_contacts.items():
                print(key, ":", value)
                
        elif option == '5':
            find = input("Enter the contact you want to find: ")
            d = find_contact(all_contacts, find)
            print(d)
        elif option == '6':
            break
        else:
            print("Invalid option")            