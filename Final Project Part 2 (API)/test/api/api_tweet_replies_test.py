import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_tweet_replies import APITweetReplies


class TestAPITweetReplies(unittest.TestCase):

    def setUp(self):
        # Arrange
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.tweet_id = self.config["tweet_id"]
        self.header = self.config["header"]

    def test_get_tweet_replies(self):
        """ checks the status code and if the test passed or not,
                         also compares the expected creation date with the one in the response body  """
        # Arrange
        tweet_replies = APITweetReplies(self.api_request)
        # Act
        tweet_replies_obj = tweet_replies.get_tweet_replies(self.url, self.header, self.tweet_id)
        # Assert
        self.assertEqual(tweet_replies_obj.status_code, 200)
        self.assertTrue(tweet_replies_obj.ok)
