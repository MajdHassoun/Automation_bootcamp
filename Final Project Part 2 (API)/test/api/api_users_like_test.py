import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_users_like import APIUsersLikes


class TestAPIUsersLikes(unittest.TestCase):

    def setUp(self):
        # Arrange
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.header = self.config["header"]
        self.username = self.config["username"]
        self.user_id = self.config["user_id2"]
        self.limit = self.config["limit"]
        self.detail_response = self.config["detail"]

    def test_get_users_like(self):
        """ checks the status code and if the test passed or not,
                                        also compares the expected detail_response with the one
                                         in the response body  """
        # Arrange
        users_likes = APIUsersLikes(self.api_request)
        # Act
        users_likes_obj = users_likes.get_users_likes(self.url, self.header,
                                                      self.limit, self.user_id)
        users_likes_body = users_likes_obj.json()
        # Assert
        self.assertEqual(self.detail_response, users_likes_body["detail"])
        self.assertEqual(users_likes_obj.status_code, 200)
        self.assertTrue(users_likes_obj.ok)
