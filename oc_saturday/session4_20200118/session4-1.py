class Movie:

    def __init__(self, title, actor, director, genre):
        self.title = title
        self.actor = actor
        self.directory = director
        self.genre = genre

    def book(self):
        print(self.title, '예약되었습니다.')


class ActionMovie(Movie):

    def __init__(self, title, actor, director, blood, nation):
        super().__init__(title, actor, director, "action")
        self.blood = blood
        self.nation = nation

    def book(self):
        super().book()
        print(self.title, "은 액션영화입니다.")

    def stressGetAway(self):
        print('스트레스가 해소되었습니다.')

malepicent = Movie("malepicent", "Angelina Jolly", "Hakyung", "Fantasy")
malepicent.book()

born = ActionMovie("Born ultimatum", "Mathew Damon", "Dohan", "YES", "America")
born.book()
