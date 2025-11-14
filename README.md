# 📘Student Record System

This is a console-based Student Record System built in Python.
It allows users to manage student records, clubs, and grade statistics using Lists, Tuples, Sets, Dictionaries, and the Math module.

## 📂 Features Overview

**✅ 1. Add Students**

**󠁯•󠁏󠁏 Inputs:**

    - Student Name
    - Age (validated to be positive number)
    - Course
    - 3 Grades (validated between 0–100)
    
󠁯•󠁏󠁏 Grades are stored as a tuple.

󠁯•󠁏󠁏 Student records are stored in a list of dictionaries.


**✅ 2. View All Students**

**Displays:**

    - Name
    - Age
    - Course
    - Grades
    - Computed Average

If there are no students, a message is shown.

**✅ 3. Manage Clubs**

Clubs are stored in a Python set.

**Includes:**

     - Add new club
     - View all clubs
     - Remove a club

Clubs cannot be duplicated because sets automatically prevent duplicates.

**✅ 4. Show Grade Statistics**

Collects all grades from every student and computes:

    - Highest grade
    - Lowest grade
    - Average grade
    - Floored average (using math.floor)
    - Square root of average (using math.sqrt)
    - Ceiling of average (using math.ceil)

Useful for demonstrating Python Math module functions.

**✅ 5. Exit**

Ends the program.

## 🧠 Program Structure - Data Structures Used

    Students – List: Stores multiple student records
    Student Data – Dictionary: Stores attributes of a student
    Grades – Tuple: Stores 3 fixed grades
    Clubs – Set: Stores unique club names

## 🧾 Menu Flow

    ===STUDENT RECORD SYSTEM===
    1. View All Students
    2. Add Students
    3. Manage Clubs
    4. Show Grade Statistics
    5. Exit

## ⚙️ How to Run

1. Save the file as:

       student_record.py

2. Open your terminal / command prompt.

3. Run the script:

        python student_record.py

## 🧮 Math Module Usage

The program uses the math library to demonstrate:

    math.floor()  # Floors the average
    math.sqrt()   # Square root of average
    math.ceil()   # Rounds average upward

## 📝 Input Validations

󠁯•󠁏󠁏 Age must be a positive integer

󠁯•󠁏󠁏 Grades must be between 0 and 100

󠁯•󠁏󠁏 Club names cannot be duplicated

󠁯•󠁏󠁏 Choices in menus must be valid numbers

These prevent user errors and program crashes.

## 📌 Example Student Entry

    Name: Jasmine
    Age: 19
    Course: BSCS
    Grades: 90, 85, 88
    Average: 87.67


## 👨‍💻 Developer Notes

󠁯•󠁏󠁏 The program loops until the user exits.

󠁯•󠁏󠁏 Student grades are stored in tuples because they do not need modification.

󠁯•󠁏󠁏 Clubs use a set, ensuring no duplicates appear.

󠁯•󠁏󠁏 Try/Except blocks handle invalid numeric inputs.
