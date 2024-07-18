import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_users_like import APIUsersLikes


class TestAPIUsersLikes(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.config = ConfigProvider.load_config_json()
        self.api_request = APIWrapper()
        self.url = self.config["url"]
        self.header = self.config["header2"]
        self.username = self.config["username"]
        self.user_id = self.config["user_id2"]
        self.limit = self.config["limit"]


    def test_users_like(self):



