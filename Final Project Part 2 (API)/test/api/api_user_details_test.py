import time
import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_user_details import APIUserDetails
from logic.api.entity.user_details import UserDetails

from parameterized import parameterized


class TestAPIUserDetails(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test environment by loading the configuration.
        """
        self.api_request = APIWrapper()
        self.config = ConfigProvider().load_config_json()
        self.username = self.config["username"]
        self.user_id = self.config["user_id1"]

    @parameterized.expand([["omarmhaimdat", "omarmhaimdat",
                            "96479162", "96479162"]])
    def test_get_user_details(self, username, expected_username, user_id, expected_user_id):
        user_details = APIUserDetails(self.api_request)
        user_details_obj = user_details.get_user_details(username, user_id)
        user_details_body = user_details_obj.json()
        self.assertEqual(expected_username, user_details_body["username"])
        self.assertEqual(expected_user_id, user_details_body["user_id"])
        self.assertEqual(user_details_obj.status_code, 200)
        self.assertTrue(user_details_obj.ok)
        time.sleep(1)

    @parameterized.expand([["omarmhaimdat", "omarmhaimdat",
                            "96479162", "96479162"]])
    def test_post_user_details(self, username, expected_username, user_id, expected_user_id):
        user_details = APIUserDetails(self.api_request)
        user_details_sent_body = UserDetails(username, user_id)
        user_details_obj = user_details.post_user_details(user_details_sent_body.to_dict())
        results = user_details_obj.json()
        self.assertEqual(expected_username, results["username"])
        self.assertEqual(expected_user_id, results["user_id"])
        self.assertEqual(user_details_obj.status_code, 200)
        self.assertTrue(user_details_obj.ok)


if __name__ == '__main__':
    unittest.main()
