class Assessment:
    def __init__(self, title, max_score):
        self.__title = title
        self.__max_score = max_score

    def get_title(self):
        return self.__title

    def get_max_score(self):
        return self.__max_score