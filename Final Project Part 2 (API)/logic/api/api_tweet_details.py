from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APITweetDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_details(self):
        url = f"{self.config['url']}/tweet/details?tweet_id={self.config['tweet_details_id']}"
        return self._request.get_request(url, headers=self.config["header"])
