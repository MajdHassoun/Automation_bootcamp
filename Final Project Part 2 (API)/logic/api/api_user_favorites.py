from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIUsersFavorites:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_users_favorites(self, url, headers, favorites_tweet_id):
        url = f"{url}/tweet/favoriters?tweet_id={favorites_tweet_id}"
        return self._request.get_request(url, headers=headers)
