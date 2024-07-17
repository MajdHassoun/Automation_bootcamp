import requests
from infra.api.api_wrapper import APIWrapper


class APIDrawCard:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_draw_card(self, url, deck_id, cards_count):
        return self._request.get_request(
            f"{url}{deck_id}/draw/?count={cards_count}")
