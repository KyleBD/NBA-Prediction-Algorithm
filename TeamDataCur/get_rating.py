from nba_api.stats.endpoints import leaguedashteamstats
from TeamDataHistorical.constants import team_ids, all_seasons
import pandas

temp_season_summary = []

total_data = []

for season in all_seasons:
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
            team_name = team_stats_data['TEAM_NAME']
            record = float(team_stats_data['W'] / team_stats_data['GP'])
            net_rating =  float(team_stats_data['PLUS_MINUS']) / 82

            print(team_name)
            print(net_rating)
            temp_season_summary.append(record)
            temp_season_summary.append(net_rating)
            total_data.append(temp_season_summary)
            temp_season_summary = []
            
        except:
            pass
    '''
    print(total_data)
    total_data = []
    '''

final_data =total_data