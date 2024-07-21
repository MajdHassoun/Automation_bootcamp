from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIGetTrendsNearLocation:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_trends_near_location(self):
        url = f"{self.config['url']}/trends/?woeid={self.config['woeid']}"
        return self._request.get_request(url, headers=self.config["header"])
