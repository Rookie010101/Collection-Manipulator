print("Welcome to the Student Data Organizer!")
students = []
while True:
    print("\nSelect an option: ")
    print('''1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit)''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter student details: ")
            ID = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            DOB = input("Date of Birth (YYYY-MM-DD): ")
            Sub = input("Subjects (comma-seperated): ")
            student = {"StudentID":ID, "name":name, "age":age, "grade":grade, "DOB":DOB, "sub":Sub}
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
            for s in students:
                for sub in s["sub"].split(","):
                    unique_sub.add(sub)
            subjects = []
            for sub in unique_sub:
                subjects.append(sub)
            for sub in subjects:
                print(f"The subjects offered are {sub}")
                
        case 6:
            print("Thankyou for using the Student Data Organizer!")
            break
