from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APISearch:
    """
    The APISearch class interacts with an API to perform search operations.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APISearch class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_search(self):
        """
        Performs a GET request to search for a specific query.

        Returns:
        The response from the API request.
        """
        url = f"{self.config['url']}/search/search?query=url_search_query_param"
        return self._request.get_request(url, headers=self.config["header"])

    def check_all_json(self, searches):
        for i in range(len(searches)):
            search_id = searches[i]["tweet_id"]
            if search_id == self.config["search_tweet_id"]:
                return search_id

    def post_search(self, search_body):
        """
        Performs a POST request to search with a specified body.

        Parameters:
        search_body (dict): The body of the POST request.

        Returns:
        The response from the API request.
        """
        return self._request.post_request(f'{self.config["url"]}/search/search', self.config["header_post"],
                                          search_body)


