import requests
from gameData import gameData
# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = '739cd0db1260420e97dbfb9d12aa5f18'

SPORT = 'basketball_ncaab'  # Use 'basketball_ncaab' for college basketball

REGIONS = 'us'  # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h,spreads'  # Include the markets you want for college basketball

ODDS_FORMAT = 'decimal'  # decimal | american

DATE_FORMAT = 'iso'  # iso | unix

# First get a list of in-season sports
sports_response = requests.get(
    'https://api.the-odds-api.com/v4/sports',
    params={
        'api_key': API_KEY
    }
)

if sports_response.status_code != 200:
    print(sports_response.status_code)

# Now get a list of live & upcoming games for college basketball along with odds
odds_response = requests.get(
    "https://api.the-odds-api.com/v4/sports/"
    + SPORT
    + "/odds" ,
    params={
        'api_key': API_KEY,
        'regions': REGIONS,
        'markets': MARKETS,
        'oddsFormat': ODDS_FORMAT,
        'dateFormat': DATE_FORMAT,
    }
)

if odds_response.status_code != 200:
    
    print(odds_response.status_code)
else:
    odds_json = odds_response.json()
    print('Number of events:', len(odds_json))
    event_list = []
    for event in odds_json:
        tempGame = gameData(event['home_team'], event['away_team'], event['bookmakers'])
        event_list.append(tempGame)
    # Check the usage quota
    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
