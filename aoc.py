from urllib import request
from os import path

def get_input(day):
    file_name = f"inputs/{day:02}.txt"

    file = open(file_name, "r")
    data = file.read()
    file.close()
    
    return data


