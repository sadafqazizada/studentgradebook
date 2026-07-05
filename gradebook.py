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