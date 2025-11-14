import math

students = [] #List
clubs = {"UMSDC","DOUM","ENIGMA","BLOCKCHAIN"} #Set

def tuples(grade_list):
   return  tuple(grade_list)

# ADD STUDENTS
def add_student():
    print("\n--Add Student--")
    name = input("Enter Student Name: ")

    while True:
        try:
            age = int(input("Enter Student Age:"))
            if age <= 0:
                print("Age must be positive!")
                continue
            break
        except ValueError:
            print("Invalid Input! Please enter a number.")

    course = input("Enter Course: ")

    print("\n---Enter 3 Grades---")
    grade_list = []
    for i in range(3):
        while True:
            try:
                grade = float(input(f"Grade {i+1}:"))
                if 0 <= grade <= 100:
                    grade_list.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100!")
            except ValueError:
                print("Invalid Input! Please enter a number.")

    grades = tuple(grade_list)

    student = {
        'name': name,
        'age': age,
        'course': course,
        'grades': grades
    }
    students.append(student)
    print(f"\nStudent '{name}'added successfully!")


# VIEW ALL STUDENTS
def view_all_students():
    if not students:
        print("\nNo Students in the system yet.")
        return

    print("---All Students Records---")

    for idx, student in enumerate(students, 1):
        print(f"\nStudent #{idx}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Grades: {student['grades'][0]}, {student['grades'][1]}, {student['grades'][2]}")
        avg = sum(student['grades']) / len(student['grades'])
        print(f"Average: {avg:.2f}")


# MANAGE CLUB
def manage_club():
    # ADD CLUB
    def club_menu():
     print("""\n--MANAGE CLUB--
1. Add a club
2. View a club
3. Remove a club
4. Back to main menu """)

    while True:
        club_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            add_clubs()
        elif choice == '2':
            view_all_clubs()
        elif choice == '3':
            remove_club()
        elif choice == '4':
            break
        else:
            print("\nInvalid Choice ! Please enter a number from 1 to 4.")

# MANAGE CLUBS (Add Clubs)
def add_clubs():
    print("\n---Add New Club---")
    club_name = input("Enter Club Name: ").strip()

    if club_name in clubs:
        print(f"\nClub '{club_name}' already exists!")
    else:
        clubs.add(club_name)
        print(f"\nClub '{club_name}' added successfully!")


# MANAGE CLUBS (View Clubs)
def view_all_clubs():
    if not clubs:
        print("\nNo clubs registered yet.")
        return

    print("\n---REGISTERED CLUBS---")
    for idx, club in enumerate(sorted(clubs), 1):
        print(f"{idx}. {club}")

# MANAGE CLUBS (Remove Clubs)
def remove_club():
    if not clubs:
        print("\nNo clubs to remove.")
        return

    view_all_clubs()
    try:
        choice = int(input("\nEnter the Number of the club to remove: "))
        clubs_list = sorted(clubs)

        if 1 <= choice <= len(clubs_list):
            club_to_remove = clubs_list[choice - 1]
            clubs.remove(club_to_remove)
            print(f"\nClub '{club_to_remove}' removed successfully!")
        else:
            print(f"\nInvalid number! Please choose between 1 and {len(clubs_list)}.")
    except ValueError:
        print("\nInvalid input! Please enter a number.")

# SHOW GRADE STATISTICS
def calculate_statistics():
    if not students:
        print("\nNo students in the system yet.")
        return

    all_grades = []

    for student in students:
        all_grades.extend(student['grades'])

    if not all_grades:
        print("\nNo grades to calculate.")
        return

    # Calculate Statistics
    highest = max(all_grades)
    lowest = min(all_grades)
    average = sum(all_grades) / len(all_grades)
    average_floored = math.floor(average)

    print("--- GRADE STATISTICS---")
    print(f"""Total number of grades: {len(all_grades)}
Highest:{highest}
Lowest: {lowest}
Average Grade: {average:.2f}
Average (floor): {average_floored} """)

    # Additional math module demonstrations
    print("\nAdditional Calculations:")
    print(f"Square root of average: {math.sqrt(average):.2f}")
    print(f"Ceiling of average    : {math.ceil(average)}")


# MAIN LOOP
def main():
    def display_menu():
     print("""\n===STUDENT RECORD SYSTEM===
1. View All Students
2. Add Students
3. Manage Clubs
4. Show Grade Statistics
5. Exit""")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_all_students()
        elif choice == '2':
            add_student()
        elif choice == '3':
            manage_club()
        elif choice == '4':
            calculate_statistics()
        elif choice == '5':
            print("Thank you for using Student Record System!")
            break
        else:
            print("\n Invalid choice! Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()