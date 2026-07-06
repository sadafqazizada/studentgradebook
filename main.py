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

#---------------------Add a quiz, exam, or project----------------------

        elif choice == "5":

            course_code = input("Course Code: ")
            assessment_type = input("Assessment Type (quiz/exam/project): ").lower()
            title = input("Assessment Title: ")
            max_score = float(input("Maximum Score: "))

 #-------------------Create the correct assessment object--------------------

            if assessment_type == "quiz":
                assessment = Quiz(title, max_score)

            elif assessment_type == "exam":
                assessment = Exam(title, max_score)

            elif assessment_type == "project":
                assessment = Project(title, max_score)

            else:
                print("Invalid assessment type.")
                continue

            gradebook.add_assessment(course_code, assessment)

 #---------------------Record a student's grade--------------------

        elif choice == "6":

            student_id = input("Student ID: ")
            course_code = input("Course Code: ")
            assessment_title = input("Assessment Title: ")
            score = float(input("Score: "))

            gradebook.record_grade(
                student_id,
                course_code,
                assessment_title,
                score
            )

#--------------------Show the student's project--------------------
        elif choice == "7":

            student_id = input("Student ID: ")

            gradebook.show_report(student_id)

#--------------------Search for a student--------------------

        elif choice == "8":

            keyword = input("Student ID or Name: ")

            student = gradebook.search_student(keyword)

            if student:

                student.display_info()

            else:

                print("Student not found.")

#--------------------Update student information--------------------

        elif choice == "9":

            student_id = input("Student ID: ")

            email = input("New Email: ")

            gradebook.update_student(student_id, email)

#--------------------Remove a student---------------------

        elif choice == "10":

            student_id = input("Student ID: ")

            gradebook.delete_student(student_id)

#-------------------Exit the Program--------------------
        elif choice == "0":

            print("Goodbye!")

            break

        