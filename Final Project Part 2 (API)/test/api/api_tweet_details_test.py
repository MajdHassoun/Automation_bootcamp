import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_tweet_details import APITweetDetails


class TestFollowers(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.tweet_details_id = self.config["tweet_details_id"]

    def test_get_tweet_details(self):
        followers = APITweetDetails(self.api_request)
        tweet_details_obj = followers.get_tweet_details(self.config['tweet_details_id'])
        tweet_details_body = tweet_details_obj.json()
        tweet_details_results = tweet_details_body["tweet_id"]
        self.assertEqual(tweet_details_results, self.tweet_details_id)
        self.assertEqual(tweet_details_obj.status_code, 200)
        self.assertTrue(tweet_details_obj.ok)
