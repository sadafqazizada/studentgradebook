#--------------------Constructor (Initialize Assessment Object)--------------------

class Assessment:

    def __init__(self, title, max_score):

        self.__title = title

        self.__max_score = max_score

#--------------------Getter Methods (Access Private Data Safely)--------------------

    def get_title(self):
        return self.__title

    def get_max_score(self):
        return self.__max_score

#--------------------Calculate Percentage--------------------

    def calculate_percentage(self, score):

        return (score / self.__max_score) * 100

#--------------------General Grade Message--------------------

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 55:

            return "Passed"

        else:

            return "Failed"

#---------------------Display Assessment Information--------------------

    def display_info(self):

        print(f"{self.__title} - max score: {self.__max_score}")

#--------------------Quiz Class (Inheritance and method Overriding)--------------------

class Quiz(Assessment):

    def display_info(self):

        print(f"Quiz: {self.get_title()} - Max Score: {self.get_max_score()}")

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 80:

            return "Great quiz result"
        else:
            return "Needs more practice"

#--------------------Exam Class (Inheritance and Method Overriding)--------------------

class Exam(Assessment):

    def display_info(self):

        print(f"Exam: {self.get_title()} - Max Score: {self.get_max_score()}")

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 55:

            return "Passed exam"

        else:

            return "Failed exam"

#--------------------Project Class (Inheritance and Method Overriding)--------------------

class Project(Assessment):

    def display_info(self):

        print(f"Project: {self.get_title()} - Max Score: {self.get_max_score()}")

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 85:

            return "Excellent project"

        elif percentage >= 55:

            return "Project submitted"

        else:

            return "Project needs improvement"