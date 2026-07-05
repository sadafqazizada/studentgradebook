class Course:
    def __init__(self, course_code, course_name):
        self.__course_code = course_code
        self.__course_name = course_name
        self.__students = []
        self.__assessments = []

    def get_course_code(self):
        return self.__course_code
    def get_course_name(self):
        return self.__course_name

    def add_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
        else:
            print(" Student is already enrolled in this course")
    def add_assessment(self, assessment):
        self.__assessments.append(assessment)