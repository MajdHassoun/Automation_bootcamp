import time
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_user_details import APIUserDetails
from logic.api.entity.user_details import UserDetails


class TestAPIUserDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration and shuffling the deck.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider().load_config_json()
        self.username = self.config["username"]
        self.user_id = self.config["user_id1"]

    def test_get_user_details(self):
        """
        Tests the shuffling of the deck by calling the API and validating the response.
        """
        user_details = APIUserDetails(self.api_request)
        user_details_obj = user_details.get_user_details()
        user_details_body = user_details.get_user_details().json()
        self.assertEqual(self.username, user_details_body["username"])
        self.assertEqual(self.user_id, user_details_body["user_id"])
        self.assertEqual(user_details_obj.status_code, 200)
        self.assertTrue(user_details_obj.ok)
        print(user_details_body)

    def test_post_user_details(self):
        user_details = APIUserDetails(self.api_request)
        user_details_body = UserDetails(self.config['username'], self.config['user_id1'])
        user_details_obj = user_details.post_user_details(user_details_body.to_dict())
        self.assertEqual(user_details_obj.status_code, 200)
        self.assertTrue(user_details_obj.ok)
