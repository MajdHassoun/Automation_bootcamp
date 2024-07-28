import json

FILE_PATH = "C:\\Users\\majdh\\OneDrive\\שולחן העבודה\\Automation_bootcamp\\advanced OOP FLASK pet task\\pet.json"


def save_data(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library.to_dict(), file)


def load_data():

    with open(FILE_PATH, 'r') as file:
        data = json.load(file)
        return data
