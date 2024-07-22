from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIUserDetails:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self, username, userid):
        url = f"{self.config['url']}/user/details?username={username}&user_id={userid}"
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_details(self, user_name_details):
        return self._request.post_request(f'{self.config["url"]}/user/details', self.config["header_post"],
                                          user_name_details)
