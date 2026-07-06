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
                count += 1
        if count == 0:
            return 0
        return total / count

    def get_result(self, average):
        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"