from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIFollowers:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_followers(self):
        url = f"{self.config['url']}/user/followers?user_id=96479162&limit=10"
        return self._request.get_request(url, headers=self.config["header"])
