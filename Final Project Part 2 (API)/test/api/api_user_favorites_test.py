import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_user_favorites import APIUsersFavorites


class TestAPIUsersFavorites(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.header = self.config["header"]
        self.user_favorites_response = self.config["user_favorites_response"]

    def test_get_users_favorites(self):
        user_favorites = APIUsersFavorites(self.api_request)
        user_favorites_obj = user_favorites.get_users_favorites(self.url, self.header)
        users_favorites_body = user_favorites_obj.json()
        self.assertEqual(self.user_favorites_response, users_favorites_body["detail"])
        self.assertEqual(user_favorites_obj.status_code, 200)
        self.assertTrue(user_favorites_obj.ok)
