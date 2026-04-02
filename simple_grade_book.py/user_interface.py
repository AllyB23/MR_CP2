# MR 1st Simple Grade Book User Interface
# import module aliases
from classes import GradeBook

def main():
    my_gradebook = GradeBook()

    while True:
        print("\n============== SIMPLE GRADE BOOK ===============")
        print("1. Add Student")
        print("2. Add grade to student")
        print("3. View Student Average")
        print("4. View Students")
        print("5. Save and Exit")

        choice = input("\nWhat would you like to do? ")

        if choice == '1':
            name = input("Enter student name: ")
            s_id = input("Enter student ID: ")
            my_gradebook.add_student(name, s_id)

        elif choice == '2':
            s_id = input("Enter student ID: ")
            try:
                score = float(input("Enter grade score: "))
                my_gradebook.add_grade_to_student(s_id, score)
                print(f"Grade {score} added.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == '3':
            s_id = input("Enter student ID: ")
            student = my_gradebook.get_student(s_id) 
            if student:
                avg = student.calculate_average()
                letter = student.get_letter_grade()
                print(f"Student {student.name} ({s_id}) Average: {avg:.2f} (Grade: {letter})")
            else:
                print("Student not found.")
        
        elif choice == '4':
            my_gradebook.show_all()
            
        elif choice == '5':
            my_gradebook.save_to_csv()
            print("Goodbye!")
            break 
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()