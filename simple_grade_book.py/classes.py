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

    def show_all(self):
        for s_id, student in self.students.items():
            print(f"ID: {s_id} | Name: {student.name} | Avg: {student.average():.2/f}")

def main_menu():
    gb = GradeBook()
    while True:
        print("Welcome To Your Gradebook!")
        print("You can add students and add their grades and edit it as you please!")
        print("1. Add student")
        print("2. ")
        choice = input("What do you want to do?")

