from nba_api.stats.endpoints import alltimeleadersgrids
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import playerdashboardbyclutch

def get_carear_data():
    #Currently returning data frame but change based off what is necissary.
    alltime_data = alltimeleadersgrids.AllTimeLeadersGrids()
    alltime_data = alltime_data.get_data_frames()[0]
    return alltime_data

class CurrentSeasonData:
    def __init__(self, player_id, season) -> None:
        self.get_player_stats_offence(player_id, season)
        self.get_player_stats_defence(player_id, season)

    def get_player_stats_offence(self, player_id, season) -> None:
        player_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        player_log_data = player_log.get_data_frames()[0]
        self.games_played = len(player_log_data)
        self.points_per_game = player_log_data['PTS'].mean()
        self.plus_minus_per_game = player_log_data['PLUS_MINUS'].mean()
        self.tov_per_game = player_log_data['TOV'].mean()
        self.assists_per_game = player_log_data['AST'].mean()
        self.fg_attempted_per_game = player_log_data['FGA'].mean()
        self.ft_attempted_per_game = player_log_data['FTA'].mean()
        self.ft_percentage_per_game = player_log_data['FT_PCT'].mean()
        self.three_fg_pct_per_game = player_log_data['FG3_PCT'].mean()
        self.fg_pct_per_game = player_log_data['FG_PCT'].mean()
        self.total_points = self.points_per_game * self.games_played
        self.fg_attempted = self.fg_attempted_per_game * self.games_played
        self.ft_attempted = self.ft_attempted_per_game* self.games_played
        self.calc_true_shooting()
        self.calc_player_score()

    def get_player_stats_defence(self, player_id, season) -> None:
        player_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        player_log_data = player_log.get_data_frames()[0]
        self.blocks = player_log_data['BLK'].mean()
        self.steals = player_log_data['STL'].mean()
    
    def calc_true_shooting(self) -> None:
        self.true_shooting = self.total_points / (2*(self.fg_attempted + 0.44*self.ft_attempted))

    def calc_player_score(self):
        self.offensive_elo = (0.5*self.true_shooting +  0.2*(self.assists_per_game) 
        - 0.15*(self.tov_per_game) + 0.15*(self.three_fg_pct_per_game)
        )



#This section will be used to get players data specifically in the last 10 seconds of games
class ClutchData:
    def __init__(self, player_id) -> None:
        self.get_player_advanced_stats_offensive(player_id)
        self.get_player_advanced_stats_deffensive(player_id)
        self.calculate_defensive_clutch()
        self.calculate_offensive_clutch()
        self.calculate_clutch_elo()

    def calculate_clutch_elo(self):
        self.elo = 0.7*(self.offensive_elo) + 0.3*(self.defensive_elo)

    def get_player_advanced_stats_offensive(self, player_id) -> None:
        advanced_stats = playerdashboardbyclutch.PlayerDashboardByClutch(player_id=player_id)
        advanced_stats_data = advanced_stats.get_data_frames()[0]
        #use the FGA values to get rid of players who have taken under an certain amount of shots if needed
        self.w_pct = advanced_stats_data["W_PCT"].mean()
        self.fga = advanced_stats_data["FGA"].mean()
        self.fg_pct = advanced_stats_data["FG_PCT"].mean()
        self.three_pt_fga = advanced_stats_data["FG3A"].mean()
        self.three_fg_pct = advanced_stats_data["FG3_PCT"].mean()
        self.fta = advanced_stats_data["FTA"].mean()
        self.ft_pct = advanced_stats_data["FT_PCT"].mean()

    def get_player_advanced_stats_deffensive(self, player_id) -> None:
        advanced_stats = playerdashboardbyclutch.PlayerDashboardByClutch(player_id=player_id)
        advanced_stats_data = advanced_stats.get_data_frames()[0]
        self.steals = advanced_stats_data["STL"].mean()
        self.blocks = advanced_stats_data["BLK"].mean()
    
    def calculate_defensive_clutch(self) -> None:
        self.defensive_elo = 2*(self.steals) + self.blocks
    def calculate_offensive_clutch(self) -> None:
        self.offensive_elo = 0.1*(self.w_pct) + 0.5*(self.fg_pct) + 0.2(self.three_fg_pct) + 0.1(self.ft_pct)



    

