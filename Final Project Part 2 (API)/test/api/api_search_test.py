import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_search import APISearch


class TestAPISearch(unittest.TestCase):

    def setUp(self):
        # Arrange
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.search_tweet_id = self.config["search_tweet_id"]

    def test_get_search(self):
        """ checks the status code and if the test passed or not,
                         also compares the expected tweet_id with the one in the response body  """
        # Arrange
        search = APISearch(self.api_request)
        # Act
        search_obj = search.get_search()
        search_body = search_obj.json()
        searches = search_body["results"]
        search_id = search.check_all_json(searches)
        # Assert
        self.assertEqual(search_id, self.search_tweet_id)
        self.assertEqual(search_obj.status_code, 200)
        self.assertTrue(search_obj.ok)

    def test_post_search(self):
        """makes a Post call, checks the status code and if the test passed or not"""
        # Arrange
        search = APISearch(self.api_request)
        search_body = self.config["search_post_body"]
        # Act
        search_obj = search.post_search(search_body)
        # Assert
        self.assertEqual(search_obj.status_code, 200)
        self.assertTrue(search_obj.ok)
