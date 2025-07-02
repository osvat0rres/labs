

def print_name(name):
    
    print(f"{"index":<8}{'first name':<22}{'last name'}")
    print("=============================================")
    for i, name in enumerate(name):
        print(f'{str(i):<8}{name[0]:<22}{name[1]}')



def add_contact(name):
   
    # This fucntion will add the first name and the last name of 
    # the contact that it is added
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
   
    name.append([first_name, last_name])
    return name

def modify_list(name):
    
    print_name(name)
    index = int(input("Enter the index you want to change: "))
    
    if 0 <= index < len(name):
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        
        name[index] = [first_name,last_name]
    else:
        print("Invalid index")
    
    return name

def delete_name(name):
    
    print_name(name)
    index = int(input("Enter the index you want to delet: "))
    
    if 0 <= index < len(name):
        
        del name[index]
    else:
        print("invalid index")
        
    return name