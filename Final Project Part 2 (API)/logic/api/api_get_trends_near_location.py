from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider


class APIGetTrendsNearLocation:
    """
    The APIGetTrendsNearLocation class interacts with an API to retrieve trends near a specific location.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APIGetTrendsNearLocation class with an APIWrapper instance and loads the configuration.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request
        self.config = ConfigProvider.load_config_json()

    def get_trends_near_location(self, woied):
        """
        Retrieves trends near a specific location based on the WOEID.

        Parameters:
        woied (str): The WOEID of the location.

        Returns:
        The response from the API request.
        """
        url = f"{self.config['url']}/trends/?woeid={woied}"
        return self._request.get_request(url, headers=self.config["header"])

