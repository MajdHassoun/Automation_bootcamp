import json


class ConfigProvider:
    @staticmethod
    def load_config_json():
        try:
            with open("C:\\Users\\majdh\\OneDrive\\שולחן העבודה\\Automation_bootcamp\\Final Project Part1\\config.json",
                      'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")
