
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider



class APIShuffleCards:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_config_json()

    def get_shuffle_cards(self):
        return self._request.get_request(
            f"{self._config['base_url']}new/shuffle/?deck_count={self._config['deck_count']}")


