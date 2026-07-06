#------------------------Constructor (Initialize Gradebook)--------------------

class Gradebook:
    def __init__(self):

        self.students = {}

        self.courses = {}

        self.grades = {}

        self.passing_grades = 55

#--------------------Add Student--------------------

    def add_student(self, student):

        self.students[student.get_id()] = student

#--------------------Add Course-------------------

    def add_course(self, course):

        self.courses[course.get_course_code()] = course

#--------------------Enroll Student in Course--------------------

    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:

            print("Student not found.")

            return

        if course_code not in self.courses:

            print("Course not found.")

            return

        student = self.students[student_id]

        course = self.courses[course_code]

        student.enroll_course(course_code)

        course.add_student(student_id)

#--------------------Add Assessment to Course--------------------

    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:

            print("Course not found.")

            return

        course = self.courses[course_code]

        course.add_assessment(assessment)

#--------------------Record Student Grade--------------------

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:

            print("Student not found.")

            return

        if course_code not in self.courses:

            print("Course not found.")

            return

        assessment = self.courses[course_code].find_assessment(assessment_title)

        if assessment is None:

            print("Assessment not found.")

            return

        if score < 0 or score > assessment.get_max_score():

            print("Invalid score.")

            return

        if student_id not in self.grades:

            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:

            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

#--------------------calculate course Average--------------------

    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:

            return 0

        if course_code not in self.grades[student_id]:

            return 0

        total = 0

        count = 0

        course = self.courses[course_code]

        for assessment in course._Course__assessments:

            title = assessment.get_title()

            if title in self.grades[student_id][course_code]:

                score = self.grades[student_id][course_code][title]

                total += assessment.calculate_percentage(score)

        if count == 0:

            return 0

        return total / count

#--------------------Get Pass or Fail Result--------------------

    def get_result(self, average):

        if average >= self.passing_grade:

            return "Passed"

        else:

            return "Failed"

#--------------------Search Student--------------------

    def search_student(self, keyword):

        for student in self.students.values():

            if (student.get_id() == keyword or

                    student.get_name().lower() == keyword.lower()):

                return student

        return None

#--------------------Delete Student--------------------

    def delete_student(self, student_id):

        if student_id not in self.students:

            print("Student not found.")

            return

        del self.students[student_id]

        if student_id in self.grades:

            del self.grades[student_id]

        for course in self.courses.values():

            if student_id in course._Course__students:

                course._Course__students.remove(student_id)

#--------------------Show Student Report-------------------

    def show_report(self, student_id):

        if student_id not in self.students:

            print("Student not found.")

            return

        student = self.students[student_id]

        print("===== Student Report =====")

        print(f"Student ID: {student.get_id()}")

        print(f"Name: {student.get_name()}")

        for course_code in self.courses:

            if (student_id in self.grades and

                    course_code in self.grades[student_id]):

                course = self.courses[course_code]

                print(f"\nCourse: {course.get_course_code()} - {course.get_course_name()}")

                print("Grades:")

                for assessment in course.get_assessments():

                    title = assessment.get_title()

                    if title in self.grades[student_id][course_code]:

                        score = self.grades[student_id][course_code][title]

                        percentage = assessment.calculate_percentage(score)

                        print(f"{title}: {score}/{assessment.get_max_score()} = {percentage:.2f}%")

                average = self.calculate_average(student_id, course_code)

                print(f"Average: {average:.2f}%")

                print(f"Result: {self.get_result(average)}")

#--------------------Calculate Letter Grade (Creative Feature 1)--------------------
    
    def get_letter_grade(self, average):

        if average >= 90:

            return "A"

        elif average >= 80:

            return "B"

        elif average >= 70:

            return "C"

        elif average >= 60:

            return "D"

        else:

            return "F"