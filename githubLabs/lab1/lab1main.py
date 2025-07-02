
from lab1contacts import*

def main():
    
    contact_list = []
    
    while True:
        print("\n     *** TUFFY TITAN CONTACT MAIN MANU")
        print("\n1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Exit program")
        
        choice = input("Enter your choice: ")  
        
        if choice == '1':
            contact_list == print_name(contact_list)  
        elif choice == '2':
            contact_list = add_contact(contact_list) 
        elif choice == '3':
            contact_list = modify_list(contact_list)
        elif choice == '4':
            contact_list
        elif choice == '5':
            break  
        else:
            print("Invalid value. Enter a number from 1-5")  


main()

