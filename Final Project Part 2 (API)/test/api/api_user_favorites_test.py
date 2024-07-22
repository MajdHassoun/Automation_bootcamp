import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_user_favorites import APIUsersFavorites


class TestAPIUsersFavorites(unittest.TestCase):

    def setUp(self):
        # Arrange
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.header = self.config["header"]
        self.user_favorites_response = self.config["user_favorites_response"]
        self.fake_user_favorites_response = self.config["fake_user_favorites_response"]

    def test_get_users_favorites(self):
        """ checks the status code and if the test passed or not,
                                also compares the expected user_favorite_response with the one
                                 in the response body  """
        # Arrange
        user_favorites = APIUsersFavorites(self.api_request)
        # Act
        user_favorites_obj = user_favorites.get_users_favorites(self.url, self.header,
                                                                self.config['favorites_tweet_id'])
        users_favorites_body = user_favorites_obj.json()
        # Assert
        self.assertEqual(self.user_favorites_response, users_favorites_body["detail"])
        self.assertEqual(user_favorites_obj.status_code, 200)
        self.assertTrue(user_favorites_obj.ok)

    def test_negative_get_users_favorites(self):
        """Negative test, checks the status code and if the test passed or not,
                                also compares the expected fake_user_favorite_response with the one
                                 in the response body  """
        # Arrange
        user_favorites = APIUsersFavorites(self.api_request)
        # Act
        user_favorites_obj = user_favorites.get_users_favorites(self.url, self.header,
                                                                self.config['favorites_tweet_id'])
        users_favorites_body = user_favorites_obj.json()
        # Assert
        self.assertEqual(user_favorites_obj.status_code, 200)
        self.assertTrue(user_favorites_obj.ok)
        self.assertNotEqual(self.fake_user_favorites_response, users_favorites_body["detail"])
