class Student:
    def __init__(self, student_id, name, email):
        self.__student_id = student_id
        self.__name = name
        self.__email = email
        self.__courses = []