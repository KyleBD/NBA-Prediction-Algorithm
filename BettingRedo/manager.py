from oddsapi import OddsApiClient
import requests

api_key = '18cd8466443d9a64626ed67081617c07'

sports_list = ['americanfootball_nfl', 'basketball_nba', 'icehockey_nhl']
# Odds markets
# h2h | spreads | totals. Multiple can be specified if comma delimited
# More info at https://the-odds-api.com/sports-odds-data/betting-markets.html
# Note only featured markets (h2h, spreads, totals) are available with the odds endpoint.
MARKETS = 'h2h,spreads'

# Odds format
# decimal | american
ODDS_FORMAT = 'decimal'
# iso | unix
DATE_FORMAT = 'iso'


class bettingManager():
    def __init__(self, key):
        '''
        init the client
        use api key from odds api
        '''
        self.key = key
        client = OddsApiClient(api_key=key)

        response = client.retrieve_sports()
        print(response.data)

    def get_response(self, sport, region, market):
        odds_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{sport}/odds', params={
            'api_key': self.key,
            'regions': region,
            'markets': market,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        })

        if odds_response.status_code != 200:
            print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

        else:
            odds_json = odds_response.json()
            print('Number of events:', len(odds_json))
            print(odds_json)

            # Check the usage quota
            print('Remaining requests', odds_response.headers['x-requests-remaining'])
            print('Used requests', odds_response.headers['x-requests-used'])


