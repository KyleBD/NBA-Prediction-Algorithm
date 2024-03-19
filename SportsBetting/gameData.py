class gameData:
    def __init__(self, homeTeam, awayTeam, bookData) -> None:
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.bookData = bookData
        self.get_seperate_books()
        self.get_game_moneyline()
        pass

    def get_seperate_books(self) -> None:
        for book in self.bookData:
            if(book['key'] == 'fanduel'):
                self.fanduel = book['markets']
                self.sportsbook = 'fanduel'
            elif(book['key'] == 'draftkings'):
                self.draftkings = book['markets']
                self.sportsbook = 'draftkings'
    
    def get_game_moneyline(self) -> None:
        if(self.sportsbook == 'fanduel'):
            self.get_bet_type_data('fanduel')
        elif(self.sportsbook == 'draftkings'):
            self.get_bet_type_data('draftkings')

    def get_bet_type_data(self, bookname):
        if(bookname == 'fanduel'):
            for betType in self.fanduel:
                if(betType['key'] == 'h2h'):
                    for data in betType['outcomes']:
                        if(self.homeTeam == data['name']):
                            self.homeTeamML = data['price']
                        
                        elif(self.awayTeam == data['name']):
                            self.awayTeamML = data['price']

                elif(betType['key'] == 'spreads'):
                    for data in betType['outcomes']:
                        if(self.homeTeam == data['name']):
                            self.homeTeamSpreadPrice = data['price']
                            self.homeTeamSpreadNum = data['point']
                        
                        elif(self.awayTeam == data['name']):
                            self.awayTeamSpreadPrice = data['price']
                            self.awayTeamSpreadNum = data['point']

        elif(bookname == 'draftkings'):
            for betType in self.draftkings:
                if(betType['key'] == 'h2h'):
                    for data in betType['outcomes']:
                        if(self.homeTeam == data['name']):
                            self.homeTeamML = data['price']
                        
                        elif(self.awayTeam == data['name']):
                            self.awayTeamML = data['price']

                elif(betType['key'] == 'spreads'):
                    for data in betType['outcomes']:
                        if(self.homeTeam == data['name']):
                            self.homeTeamSpreadPrice = data['price']
                            self.homeTeamSpreadNum = data['point']
                        
                        elif(self.awayTeam == data['name']):
                            self.awayTeamSpreadPrice = data['price']
                            self.awayTeamSpreadNum = data['point']

