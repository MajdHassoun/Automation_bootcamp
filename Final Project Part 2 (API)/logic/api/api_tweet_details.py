from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APITweetDetails:
    """
    The APITweetDetails class interacts with an API to retrieve details of a specific tweet.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APITweetDetails class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_details(self, tweet_details_id):
        """
        Retrieves details of a tweet based on the tweet ID.

        Parameters:
        tweet_details_id (str): The ID of the tweet.

        Returns:
        The response from the API request.
        """
        url = f"{self.config['url']}/tweet/details?tweet_id={tweet_details_id}"
        return self._request.get_request(url, headers=self.config["header"])
