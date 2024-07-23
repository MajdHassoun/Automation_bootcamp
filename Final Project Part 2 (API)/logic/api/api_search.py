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

    @staticmethod
    def check_all_json_search(searches):
        # Filter the searches to include only those that contain "#python"
        filtered_searches = list(filter(lambda search: "#python" not in search["text"], searches))

        # Check if the number of filtered results is equal to the total number of results
        if len(filtered_searches) == len(searches):
            return True
        else:
            return False

    def post_search(self, search_body):
        """
        Performs a POST request to search with a specified body.

        Parameters:
        search_body (dict): The body of the POST request.

        Returns:
        The response from the API request.
        """
        return self._request.post_request(f'{self.config["url"]}/search/search', self.config["header"],
                                          search_body)
