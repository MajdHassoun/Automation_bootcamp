import json

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APISearch:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_search(self):
        url = f"{self.config['url']}/search/search?query=%23python&section=top"f"&min_retweets=1&min_likes=1&limit=5&start_date=2022-01-01&language=en"
        return self._request.get_request(url, headers=self.config["header"])

    def post_search(self, search_body):
        return self._request.post_request(f'{self.config["url"]}/search/search', self.config["header_post"],
                                          json.dumps(search_body))
