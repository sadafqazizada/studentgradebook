from gradebook import Gradebook
from student import Student
from course import Course
from assessment import Quiz, Exam, Project

#--------------------Create the main Gradebook object--------------------

def main():

    gradebook = Gradebook()

#--------------------Main menu loop--------------------

    while True:
        print("\n===== Student Gradebook Manager =====")

        print("1. Add Student")

        print("2. View Students")

        print("3. Add Course")

        print("4. Enroll Student in Course")

        print("5. Add Assessment")

        print("6. Record Grade")

        print("7. View Student Report")

        print("8. Search Student")

        print("9. Update Student")

        print("10. Delete Student")

        print("0. Exit")

        choice = input("Choose an option: ")

#--------------------Add a new student--------------------

        if choice == "1":
            student_id = input("Student ID: ")

            name = input("Name: ")

            email = input("Email: ")

            student = Student(student_id, name, email)

            gradebook.add_student(student)

#--------------------Display all registered students--------------------
        elif choice == "2":

            gradebook.view_students()

#--------------------Create and add a new course--------------------
        elif choice == "3":

            course_code = input("Course Code: ")

            course_name = input("Course Name: ")

            course = Course(course_code, course_name)

            gradebook.add_course(course)

#---------------------Enroll a student in a course--------------------

        elif choice == "4":

            student_id = input("Student ID: ")

            course_code = input("Course Code: ")

            gradebook.enroll_student(student_id, course_code)

        