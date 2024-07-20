import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_tweet_replies import APITweetReplies


class TestAPITweetReplies(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.tweet_id = self.config["tweet_id"]
        self.header = self.config["header"]

    def test_get_tweet_replies(self):
        tweet_replies = APITweetReplies(self.api_request)
        tweet_replies_obj = tweet_replies.get_tweet_replies(self.url, self.header, self.tweet_id)
        tweet_replies_body = tweet_replies_obj.json()
        replies = tweet_replies_body["replies"]
        reply_creation_date = replies[0]["creation_date"]
        self.assertEqual(reply_creation_date, self.config["creation_date"])
        self.assertEqual(tweet_replies_obj.status_code, 200)
        self.assertTrue(tweet_replies_obj.ok)

