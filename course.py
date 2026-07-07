#--------------------Constructor (Initialize Course Object)---------------------

class Course:

    def __init__(self, course_code, course_name):

        self.__course_code = course_code

        self.__course_name = course_name

        self.__students = []

        self.__assessments = []

#--------------------Getter Methods (Access Course Information)--------------------

    def get_course_code(self):

        return self.__course_code

    def get_course_name(self):

        return self.__course_name

#--------------------Manage Student and Assessments--------------------

    def add_student(self, student):

        if student not in self.__students:

            self.__students.append(student)

        else:

            print(" Student is already enrolled in this course")

    def add_assessment(self, assessment):
        self.__assessments.append(assessment)

#--------------------Find Assessment by Title--------------------

    def find_assessment(self, assessment_title):

        for assessment in self.__assessments:

            if assessment.get_title() == assessment_title:

                return assessment

        return None

#--------------------Display Course Information--------------------

    def display_info(self):

        print("=====Course Information=====")

        print(f"Course Code: {self.__course_code}")

        print(f"Course Name: {self.__course_name}")

        print(f"Students Enrolled: {len(self.__students)}")

        print(f"Assessments: {len(self.__assessments)}")