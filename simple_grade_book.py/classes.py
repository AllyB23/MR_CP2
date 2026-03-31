# MR 1st simple grade book
import csv

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

class GradeBook:
    def __init__(self):
        # Maps student_id to the Student object
        self.students = {}

    def add_student(self, name, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, student_id)
        else:
            print("Student ID already exists.")

    def add_grade_to_student(self, student_id, score):
        if student_id in self.students:
            self.students[student_id].add_grade(score)
        else:
            print("Student not found")

    def show_all(self):
        if not self.students:
            print("Gradebook is empty.")
            return
        
        for s_id, student in self.students.items():
            # Fixed the .2f syntax here
            print(f"ID: {s_id} | Name: {student.name} | Avg: {student.average():.2f}")

        def save_to_csv(self, filename="grades.csv"):
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(['Student ID', 'Name', 'Grades', 'Average'])
            
            for s_id, student in self.students.items():
                # Join the list of grades into a single string like "85, 90, 78"
                grades_str = ", ".join(map(str, student.grades))
                writer.writerow([
                    s_id, 
                    student.name, 
                    grades_str, 
                    f"{student.average():.2f}"
                ])
        print(f"Data successfully saved to {filename}")