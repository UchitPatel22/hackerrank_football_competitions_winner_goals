import requests

url = 'https://jsonmock.hackerrank.com/api/football_competitions'
url1 = 'https://jsonmock.hackerrank.com/api/football_matches'


def getGoals(competition, year):
    total_goals = 0
    
    # Get winner team name
    param = {
        'competition': competition,
        'year': year,
    }

    data = requests.get(url=url, params=param).json()

    team1 = data['data'][0]['winner']
    team2 = data['data'][0]['runnerup']

    

    param1 = {
        'competition': competition,
        'year': year,
        'team1': team1,
    }

    data1 = requests.get(url=url1, params=param1).json()

    total_page = data1['total_pages']
    perPage = data1['per_page']

# Get winner team data as team 1 and team 2
    for page in range(1, total_page + 1):
        param2a = {
            'competition': competition,
            'year': year,
            'team1': team1,
            'page': page,
        }
        param2b = {
            'competition': competition,
            'year': year,
            'team2': team1,
            'page': page,
        }
        data2 = requests.get(url=url1, params=param2a).json()
        data3 = requests.get(url=url1, params=param2b).json()

        try:
            for j in range(0, perPage):

                total_goals += int(data2['data'][j]['team1goals'])
                total_goals += int(data3['data'][j]['team2goals'])

        except:
            pass

    return total_goals


print(getGoals(competition='UEFA Champions League', year=2011))


