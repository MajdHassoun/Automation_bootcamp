from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APITweetReplies:
    """
    The APITweetReplies class interacts with an API to retrieve replies to a specific tweet.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APITweetReplies class with an APIWrapper instance.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_tweet_replies(self, url, headers, tweet_id):
        """
        Retrieves replies to a tweet based on the tweet ID.

        Parameters:
        url (str): The base URL for the API.
        headers (dict): The headers to include in the API request.
        tweet_id (str): The ID of the tweet.

        Returns:
        The response from the API request.
        """
        url = f"{url}/tweet/replies?tweet_id={tweet_id}"
        return self._request.get_request(url, headers=headers)

    def check_all_json_reply(self, replies):
        for i in range(len(replies)):
            reply_date = replies[i]["creation_date"]
            if reply_date == self.config["creation_date"]:
                return reply_date
