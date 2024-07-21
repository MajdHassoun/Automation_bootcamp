import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_search import APISearch


class TestAPISearch(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.search_tweet_id = self.config["search_tweet_id"]

    def test_get_search(self):
        search = APISearch(self.api_request)
        search_obj = search.get_search()
        search_body = search_obj.json()
        searches = search_body["results"]
        search_id = searches[0]["tweet_id"]
        self.assertEqual(search_id, self.search_tweet_id)
        self.assertEqual(search_obj.status_code, 200)
        self.assertTrue(search_obj.ok)

    def test_post_search(self):
        search = APISearch(self.api_request)
        search_body = self.config["search_post_body"]
        search_obj = search.post_search(search_body)
        search_result = search_obj.json()
        self.assertEqual(search_obj.status_code, 200)
        self.assertTrue(search_obj.ok)

