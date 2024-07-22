from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIUserDetails:
    """
    The APIUserDetails class interacts with an API to retrieve and post details of a specific user.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APIUserDetails class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_user_details(self, username, userid):
        """
        Retrieves details of a user based on the username and user ID.

        Parameters:
        username (str): The username of the user.
        userid (str): The ID of the user.

        Returns:
        The response from the API request.
        """
        url = f"{self.config['url']}/user/details?username={username}&user_id={userid}"
        return self._request.get_request(url, headers=self.config["header"])

    def post_user_details(self, user_name_details):
        """
        Posts user details to the API.

        Parameters:
        user_name_details (dict): The user details to post.

        Returns:
        The response from the API request.
        """
        return self._request.post_request(
            f'{self.config["url"]}/user/details',
            self.config["header_post"],
            user_name_details
        )