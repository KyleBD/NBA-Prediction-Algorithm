from nba_api.stats.endpoints import leaguedashteamstats
from constants import team_ids, current_season, all_seasons, past_ten_seasons
import pandas

temp_season_summary = []

total_data = []

for season in current_season:
    for team in team_ids:
        try:
            team_stats = leaguedashteamstats.LeagueDashTeamStats(
                season= season,
                team_id_nullable=team
            )

            '''
            type of data [
                ["TEAM_NAME", "RECORD", "NET_RATING"] 
                ["TEAM_NAME", "RECORD", "NET_RATING"] ......
                ]
            '''


            team_stats_data = team_stats.get_data_frames()[0]
            team_name = team_stats_data['TEAM_NAME'].to_string()
            team_name = team_name.lstrip('0')

            record = float(team_stats_data['W'] / team_stats_data['GP'])
            net_rating =  float(team_stats_data['PLUS_MINUS']) / float(team_stats_data['GP'])
            assists = float(team_stats_data['AST'])
            turnover = float(team_stats_data['TOV'])

            assist_tov_ratio = assists / turnover
            shooting_data = float(team_stats_data['FGM']) + (float(team_stats_data['FG3M']) * 0.5)
            shooting = shooting_data / float(team_stats_data['FGA'])
            data = (0.8*net_rating + 0.2*shooting + 0.1*assist_tov_ratio)

            temp_season_summary.append(record)
            temp_season_summary.append(data)
            print(team_name)
            print(temp_season_summary)
            total_data.append(temp_season_summary)
            temp_season_summary = []
            
        except:
            print('#############')
            pass
    '''
    print(total_data)
    total_data = []
    '''
final_data =total_data