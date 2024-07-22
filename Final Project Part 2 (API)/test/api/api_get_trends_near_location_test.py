import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_get_trends_near_location import APIGetTrendsNearLocation


class TestFollowers(unittest.TestCase):

    def setUp(self):
        # Arrange
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.trend_name = self.config["trend_name"]

    def test_get_trends_near_location(self):
        """ checks the status code and if the test passed or not,
                 also compares the expected trend name with the one in the response body  """
        # Arrange
        trend = APIGetTrendsNearLocation(self.api_request)
        # Act
        trend_obj = trend.get_trends_near_location(self.config['woeid'])
        trend_body = trend_obj.json()
        trends = trend_body[0]
        trend_list = trends["trends"]
        trend_name = trend.check_all_json_trend(trend_list)
        # Assert
        self.assertEqual(trend_name, self.trend_name)
        self.assertEqual(trend_obj.status_code, 200)
        self.assertTrue(trend_obj.ok)
