import json
import os

FILE_NAME = "students.json"

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
        }

    @staticmethod
    def from_dict(data):
        return Student(data["student_id"], data["name"], data["age"], data["major"])


def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Student.from_dict(item) for item in data]
    except Exception:
        return []


def save_data(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=2)


def find_student(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None


def add_student(students):
    student_id = input("Student ID: ").strip()
    if not student_id:
        print("Student ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("Student with this ID already exists.")
        return
    name = input("Name: ").strip()
    age = input("Age: ").strip()
    major = input("Major: ").strip()
    students.append(Student(student_id, name, age, major))
    save_data(students)
    print("Student added.")


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    student = find_student(students, student_id)
    if student:
        print("Student ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Major:", student.major)
    else:
        print("Student not found.")


def delete_student(students):
    student_id = input("Enter student ID to delete: ").strip()
    student = find_student(students, student_id)
    if student:
        students.remove(student)
        save_data(students)
        print("Student deleted.")
    else:
        print("Student not found.")


def list_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print("ID:", student.student_id, "Name:", student.name, "Age:", student.age, "Major:", student.major)


def main():
    students = load_data()
    while True:
        print("\n1. Add student")
        print("2. Search student")
        print("3. Delete student")
        print("4. List all students")
        print("5. Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
