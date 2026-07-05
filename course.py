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