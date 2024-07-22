import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_followers import APIFollowers


class TestFollowers(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.follower_name = self.config["follower_username"]

    def test_get_followers(self):
        followers = APIFollowers(self.api_request)
        followers_obj = followers.get_followers(self.config["followers_user_id"])
        followers_body = followers_obj.json()
        followers_results = followers_body["results"]
        follower_name = followers_results[0]["username"]
        self.assertEqual(follower_name, self.follower_name)
        self.assertEqual(followers_obj.status_code, 200)
        self.assertTrue(followers_obj.ok)
