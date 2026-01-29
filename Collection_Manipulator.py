print("Welcome to the Student Data Organizer!")
students = []
while True:
    print("\nSelect an option: ")
    print('''1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter student details: ")
            ID = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            allowed_grades = ("A","B","C","D","E")
            while True:
                grade = input("Grade: ").upper()
                if grade in allowed_grades:
                    break
                else:
                    print("Please enter only A,B,C,D or E")
            while True:
                DOB = input("Date of Birth (YYYY-MM-DD): ")
                parts = DOB.split("-")
                if len(parts)!= 3 or len(parts[0])!=4 or len(parts[1])!=2 or len(parts[2])!=2:
                    print("Invalid format")
                    continue
                else:
                    year = int(parts[0])
                    month = int(parts[1])
                    date = int(parts[2])
                if not (1<=month<=12):
                    print("Month should be between 1 and 12")
                current_year = 2026
                if (current_year-year)!=age:
                    print(f"Year: {year} doesn't match with age: {age}")
                    continue
                if not 5<(current_year-year)<90:
                    print("Not Eligible for schooling")
                    continue
                odd_months = [1,3,5,7,8,10,12]
                even_months = [4,6,9,11]
                if month in odd_months:
                    max_days = 31
                elif month in even_months:
                    max_days = 30
                else:
                    if year%4==0:
                        max_days = 29
                    else:
                        max_days = 28
                if 0<date<=max_days:
                    break
                else:
                    print(f"DD: {date} is not valid")
            Sub = input("Subjects (comma-seperated): ")
            identity = (ID, DOB)
            student = {"StudentID":identity[0], "name":name, "age":age, "grade":grade, "DOB":identity[1], "sub":Sub}
            students.append(student)
            print("\nStudent added successfully!")
        case 2:
            if len(students)==0:
                print("No Student Added, Please add student!")
            else:
                print("---Details of All Student---")
                for s in students:
                    print(f'''Student ID:{s["StudentID"]} | Name:{s["name"]} | Age=>{s["age"]} | Grade=>{s["grade"]} | Date of Birth=>{s["DOB"]} | Subjects=>{s["sub"]}''')
                    print()
        case 3:
            stid = int(input("Enter the Student ID: "))
            for s in students:
                if s["StudentID"]==stid:
                     print('''1. Update Name
2. Update Age
3. Update Grade
4. Update Subjects''')
                     choice = int(input("Enter your choice: "))
                     match choice:
                        case 1:
                            new_name = input("Enter the new name: ")
                            s["name"] = new_name
                            print("Name Updated Successfully!")
                        case 2:
                            new_age = int(input("Enter the new age: "))
                            s["age"] = new_age
                            print("Age Updated Successfully!")
                        case 3:
                            new_grade = input("Enter the new grade: ")
                            s["grade"] = new_grade
                            print("Grade Updated Successfully!")
                        case 4:
                            new_subjects = input("Enter the new subjects: ")
                            s["sub"] = new_subjects
                            print("New Subjects Updated Successfully!")
                        case _:
                            print("Invalid Choice")
                print("Student ID not found...")
        case 4:
            stid = int(input("Enter the Student ID to be deleted: "))
            found = False
            print("No student found")
            
            for i in range(len(students)):
                if students[i]["StudentID"]==stid:
                    print(f"Deleting {stid}")
                    del students[i]
                    found = True
                    break
        case 5:
            unique_sub = set()
            for student in students:
                subject = student["sub"].split(", ")
                for s in subject:
                    unique_sub.add(s)
            unique_sub_list = list(unique_sub)
            print(f"Unique subjects offered are: {unique_sub_list}")    
        case 6:
            print("Thankyou for using the Student Data Organizer!")
            break
