class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grades = 55

    def add_student(self, student):
        self.students[student.get_id()] = student

    def add_course(self, course):
        self.courses[course.get_course_code()] = course

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

    def add_assessment(self, course_code, assessment):
        if course_code not in self.courses:
            print("Course not found.")
            return

        course = self.courses[course_code]
        course.add_assessment(assessment)
