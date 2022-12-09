import requests
import session


def get_input(day, year = 2022):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {
        'cookie': 'session={0}'.format(session.session)
    }
    input_values = requests.get(url, headers=headers).text.splitlines()

    return input_values