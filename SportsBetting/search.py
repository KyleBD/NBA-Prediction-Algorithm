from betting import event_list

def search_game(teamName):
    for event in event_list:
        if(teamName == event.homeTeam):
            print(teamName)
        elif(teamName == event.awayTeam):
            print(teamName)