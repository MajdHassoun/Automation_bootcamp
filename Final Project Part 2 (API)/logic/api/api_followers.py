from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIFollowers:
    """
    The APIFollowers class interacts with an API to retrieve the followers of a specific user.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APIFollowers class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_followers(self, user_id):
        """
        Retrieves the followers of a user based on their user ID.

        Parameters:
        user_id (str): The ID of the user whose followers are to be retrieved.

        Returns:
        The response from the API request.
        """
        url = f"{self.config['url']}/user/followers?{user_id}"
        return self._request.get_request(url, headers=self.config["header"])





