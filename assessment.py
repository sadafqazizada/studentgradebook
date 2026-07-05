class Assessment:
    def __init__(self, title, max_score):
        self.__title = title
        self.__max_score = max_score

    def get_title(self):
        return self.__title

    def get_max_score(self):
        return self.__max_score

class Quiz(Assessment):
    def display_info(self):
        print("=====Quiz Information=====")
        print(f"Title: {self.get_title()}")
        print(f"Max score: {self.get_max_score()}")

class Exam(Assessment):
    def display_info(self):
        print("=====Exam Information=====")
        print(f"Title: {self.get_title()}")
        print(f"Max score: {self.get_max_score()}")