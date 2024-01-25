from nba_api.stats.endpoints import commonallplayers

def get_all_time_player_ids():
    all_players = commonallplayers.CommonAllPlayers()
    all_players_data = all_players.get_data_frames()[0]

    player_ids = all_players_data['PERSON_ID'].tolist()

    return player_ids


def get_player_ids_for_season(season):
    all_players = commonallplayers.CommonAllPlayers(is_only_current_season=1, season=season)
    all_players_data = all_players.get_data_frames()[0]

    player_ids = all_players_data['PERSON_ID'].tolist()

    return player_ids

