from nba_api.stats.endpoints import assistleaders

assist_leaders = assistleaders.AssistLeaders(
    season = "2023-24"
)

assist_data = assist_leaders.get_data_frames()[0]
