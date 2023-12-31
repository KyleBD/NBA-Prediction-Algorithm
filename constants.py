from nba_api.stats.static.teams import get_teams


def list_team_ids():
    team_ids = []
    data = get_teams()
    for team in data:
        team_ids.append(team['id'])
    
    return team_ids

current_season = [
    "2023-24"
]

past_ten_seasons = [
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
]

all_seasons = [
    "1996-97",
    "1997-98",
    "1998-99",
    "1999-00",
    "2000-01",
    "2001-02",
    "2002-03",
    "2003-04",
    "2004-05",
    "2005-06",
    "2006-07",
    "2007-08",
    "2008-09",
    "2009-10",
    "2010-11",
    "2011-12",
    "2012-13",
    "2013-14",
    "2014-15",
    "2015-16",
    "2016-17",
    "2017-18",
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
]

'''
########### TEST ###########

past_ten_seasons = ["2020-21"]

team_ids = ["1610612752"]

########### TEST ###########
'''

team_ids = list_team_ids()