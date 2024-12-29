import requests
import os

SESSION = ''
YEAR = 2024

def download_input(year, day):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    resp = requests.get(url, cookies={'session': SESSION})
    resp.raise_for_status()
    inp = resp.text
    if inp[-1] == '\n': inp = inp[:-1]
    return inp

def input(day):
    path = f'input{day}.txt'
    if not os.path.exists(path):
        inp = download_input(YEAR, day)
        with open(path, 'w') as f:
            f.write(inp)
    with open(path) as f:
        return f.read()
