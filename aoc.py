
from os import path
import requests

SESSION_FILE = "session.txt"


def get_input(day, small=False):

    if small:
        file_name = f"inputs/{day:02}.small.txt"
    else:
        file_name = f"inputs/{day:02}.txt"

    if path.exists(file_name) or small:
        file = open(file_name, "r")
        data = file.read()
        file.close()
    else:
        file = open(SESSION_FILE, "r")
        session = file.read()
        file.close()
        cookies = {"session": session}

        url = f"https://adventofcode.com/2021/day/{day}/input"

        data = requests.get(url, cookies=cookies).text

        file = open(file_name, "w")
        file.write(data)
        file.close()

    return data
