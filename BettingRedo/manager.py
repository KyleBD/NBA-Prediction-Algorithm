from oddsapi import OddsApiClient

api_key = '18cd8466443d9a64626ed67081617c07'



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
        ednpoint = '/v3/odds/?apiKey={apiKey}&sport={sport}&region={region}&mkt={mkt}'
