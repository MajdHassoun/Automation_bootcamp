from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIUsersFavorites:
    """
    The APIUsersFavorites class interacts with an API to retrieve users who favorited a specific tweet.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APIUsersFavorites class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_users_favorites(self, url, headers, favorites_tweet_id):
        """
        Retrieves users who favorited a tweet based on the tweet ID.

        Parameters:
        url (str): The base URL for the API.
        headers (dict): The headers to include in the API request.
        favorites_tweet_id (str): The ID of the tweet.

        Returns:
        The response from the API request.
        """
        url = f"{url}/tweet/favoriters?tweet_id={favorites_tweet_id}"
        return self._request.get_request(url, headers=headers)
