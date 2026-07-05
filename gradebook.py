class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grades = 55

    def add_student(self, student):
        self.students[student.get_id()] = student