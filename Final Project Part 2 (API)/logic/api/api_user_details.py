import json

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIUserDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self):
        url = f"{self.config['url']}/user/details?username={self.config['username']}&user_id={self.config['user_id1']}"
        return self._request.get_request(url, headers=self.config["header1"])

    def post_user_details(self, user_name_details):
        return self._request.post_request(f'{self.config["url"]}/user/details', self.config["header_post_details"],
                                          json.dumps(user_name_details))
