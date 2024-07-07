import random
from enum import Enum


class UtilesLogic(Enum):
    ADDRESSES = [
        "Herzl St 19, Tel Aviv-Yafo",
        "Ben Yehuda St 34, Jerusalem",
        "Rothschild Blvd 8, Haifa"
    ]
    CITIES = [
        "Tel Aviv-Yafo",
        "Jerusalem",
        "Haifa"
    ]
    STATES = [
        "Tel Aviv District",
        "Jerusalem District",
        "Haifa District"
    ]
    ZIP_CODES = [
        "6433201",
        "9435001",
        "3499000"
    ]

    SSNS = [
        "123456789",
        "987654321",
        "567890123"
    ]

    @staticmethod
    def get_random_israel_detail(detail_type):
        try:
            detail_list = UtilesLogic[detail_type].value
            return random.choice(detail_list)
        except KeyError:
            raise ValueError(
                "Invalid detail type. Please choose from ADDRESSES, CITIES, STATES, ZIP_CODES, PHONES, or SSNS.")
