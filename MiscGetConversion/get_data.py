from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.endpoints import leaguegamefinder

def get_player_name(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_info_data = player_info.get_data_frames()[0]

    if not player_info_data.empty:
        player_name = f"{player_info_data['FIRST_NAME']} {player_info_data['LAST_NAME']}"
        return player_name
    else:
        return "Player not found"

def get_team_roster(team_id):
    team_info = commonteamroster.CommonTeamRoster(team_id=team_id)
    team_info_data = team_info.get_data_frames()[0]
    return team_info_data #Note data is currently not formatted. format later according to usage case

def get_team_name(team_id):
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    games_data = game_finder.get_data_frames()[0]

    if not games_data.empty:
        team_name = games_data['TEAM_NAME'].iloc[0]
        return team_name
    else:
        return "Team not found"
