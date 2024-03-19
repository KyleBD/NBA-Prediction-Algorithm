class gameData:
    def __init__(self, homeTeam, awayTeam, bookData) -> None:
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.bookData = bookData
        pass
    def get_seperate_books(self) -> None:
        for book in self.bookData:
            print(book)
            if(book['key'] == 'fanduel'):
                self.fanduel = book['key']
            elif(book['key'] == 'draftkings'):
                self.draftkings = book['key']