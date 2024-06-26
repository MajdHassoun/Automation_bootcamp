import json
from library import Library

FILE_PATH = 'library.json'

def save_library(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library.to_dict(), file)


def load_library():
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            return Library.from_dict(data)
    except FileNotFoundError:
        return Library()
