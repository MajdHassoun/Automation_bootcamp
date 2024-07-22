import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_get_trends_near_location import APIGetTrendsNearLocation


class TestFollowers(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.trend_name = self.config["trend_name"]

    def test_get_trends_near_location(self):
        trend = APIGetTrendsNearLocation(self.api_request)
        trend_obj = trend.get_trends_near_location(self.config['woeid'])
        trend_body = trend_obj.json()
        trends = trend_body[0]
        trend_list = trends["trends"]
        trend_trend = trend_list[4]
        trend_name = trend_trend["name"]
        self.assertEqual(trend_name, self.trend_name)
        self.assertEqual(trend_obj.status_code, 200)
        self.assertTrue(trend_obj.ok)
