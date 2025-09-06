
from people import Faculty,Student

# display_menu function to display the menu on console
def display_menu():
    print()
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("9. Exit the program")

if __name__ == "__main__":

    # declare an empty lists to store data
    faculties = []
    students = []

    while True:
        display_menu()

        # get user's choice
        choice = int(input("Enter menu choice: "))

        # add faculty 
        if choice == 1:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            department = input("Enter department: ")

            F = Faculty(first_name,last_name,department)
            faculties.append(F)

        # print faculty
        elif choice == 2:
            print()
            print("="*25+" FACLUTY "+"="*25)
            print()
            print("{0:<7} {1:<20} {2:<30}".format("Record","Name","Department"))
            print("="*7+" "+"="*20+" "+"="*30)

            for index in range(len(faculties)):

                faculty = faculties[index]
                print("{0:<7} {1:<20} {2:<30}".format(index,faculty.firstname+" "+faculty.lastname,faculty.department))
            
        # add student
        elif choice == 3:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            classyear = input("Enter class year: ")
            major = input("Enter major: ")
            faculty_advisor = int(input("Enter faculty advisor: "))

            S = Student(first_name,last_name)
            S.set_class(classyear)
            S.set_major(major)
            S.set_advisor(faculties[faculty_advisor])
            students.append(S)

        # print student
        elif choice == 4:
            
            print()
            print("="*40+" STUDENTS "+"="*40)
            print()
            print("{0:<20} {1:<15} {2:<30} {3:<20}".format("Name","Class","Major","Advisor"))
            print("="*20+" "+"="*15+" "+"="*30+" "+"="*20)

            for index in range(len(students)):

                student = students[index]
                print("{0:<20} {1:<15} {2:<30} {3:<20}".format(student.firstname+" "+student.lastname,student.classyear,student.major,student.advisor.firstname+" "+student.advisor.lastname))

        elif choice == 9:
            break
        else:
            print("Invalid choice")



            
