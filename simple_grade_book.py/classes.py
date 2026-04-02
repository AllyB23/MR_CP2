# MR 1st simple grade book
import csv

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
            print("Student added successfully!")
        else:
            print("Error: Student ID already exists.")

    def add_grade_to_student(self, student_id, score):
        if student_id in self.students:
            self.students[student_id].add_grade(score)
        else:
            print("Error: Student not found.")

    def get_student(self, student_id):
        return self.students.get(student_id)

    def show_all(self):
        if not self.students:
            print("Gradebook is empty.")
            return
        
        for s_id, student in self.students.items():
            avg = student.calculate_average()
            print(f"ID: {s_id} | Name: {student.name} | Avg: {avg:.2f} ({student.get_letter_grade()})")

    def save_to_csv(self, filename="grades.csv"):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Student ID', 'Name', 'Grades', 'Average'])
                for s_id, student in self.students.items():
                    grades_str = ", ".join(map(str, student.grades))
                    writer.writerow([s_id, student.name, grades_str, f"{student.calculate_average():.2f}"])
            print(f"Data successfully saved to {filename}")
        except IOError as e:
            print(f"Could not save file: {e}")