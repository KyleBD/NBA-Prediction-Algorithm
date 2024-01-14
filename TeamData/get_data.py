from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import teamdashboardbygeneralsplits


# Today's Score Board
games = scoreboard.ScoreBoard()
# json
games.get_json()


all_games = games.get_dict()["scoreboard"]["games"]


def get_daily_team_ids():
    temp_team_id = []
    daily_team_id = []
    for game in all_games:
        temp_team_id.append(game["homeTeam"]["teamId"])
        temp_team_id.append(game["awayTeam"]["teamId"])
        daily_team_id.append(temp_team_id)
        temp_team_id = []
    return daily_team_id


def get_daily_game_ids():
    daily_game_id = []
    for game in all_games:
        daily_game_id.append(game["gameId"])
    return daily_game_id


"""
today_matchups = []
temp_matchup = []
home_team_name_id = {}
away_team_name_id = {}

for game in all_games:
    home_team_name_id[game['homeTeam']['teamId']] = game['homeTeam']['teamCity']
    away_team_name_id[game['awayTeam']['teamId']] = game['awayTeam']['teamCity']
    temp_matchup.append(home_team_name_id)
    temp_matchup.append(away_team_name_id)
    today_matchups.append(temp_matchup)
    temp_matchup = []
    team_name_id = {}
    home_team_name_id = {}
    away_team_name_id = {}

print(today_matchups)
"""


def get_team_stats(team_id) -> dict:  # get all of the stats we need for calculations
    team_stats = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(
        team_id=team_id
    )
    data = team_stats.get_dict()["resultSets"]

    team_data = {}

    for data_set in data:
        if (
            data_set["name"] == "OverallTeamDashboard"
        ):  # get the overall data of the season. There are also different data sets here for different purposes
            for index, header in enumerate(data_set["headers"]):
                team_data[header] = data_set["rowSet"][0][index]

    return team_data


def set_matchups():
    daily_team_id = get_daily_team_ids()

    for game in daily_team_id:
        for team in game:
            get_team_stats(team)


