import time

from infra.api.api_wrapper import APIWrapper
from infra.api.config_provider import ConfigProvider
from logic.api.api_tweet_details import APITweetDetails
from logic.api.api_followers import APIFollowers
from logic.api.api_user_details import APIUserDetails


class Responses:

    def __init__(self):
        self.config = ConfigProvider.load_config_json()
        self.username = self.config['username']
        self.user_id = self.config['user_id1']
        self.tweet_details_id = self.config['tweet_details_id']
        self.followers_user_id = self.config['followers_user_id']
        self.api_request = APIWrapper()

    def get_user_response(self, detail):
        user_details = APIUserDetails(self.api_request)
        user_details_obj = user_details.get_user_details(self.username, self.user_id)
        user_response_body = user_details_obj.json()

        if detail == "user id":
            time.sleep(1)
            return user_response_body["user_id"]
        elif detail == "user name":
            time.sleep(1)
            return user_response_body["username"]
        elif detail == "creation date":
            time.sleep(1)
            return user_response_body["creation_date"]
        elif detail == "following count":
            time.sleep(1)
            return user_response_body["following_count"]
        elif detail == "follower_count":
            time.sleep(1)
            return user_response_body["follower_count"]

    def get_tweet_response(self, detail):
        followers = APITweetDetails(self.api_request)
        tweet_details_obj = followers.get_tweet_details(self.tweet_details_id)
        tweet_response_body = tweet_details_obj.json()
        if detail == "tweet id":
            time.sleep(1)
            return tweet_response_body["tweet_id"]
        elif detail == "creation_date":
            time.sleep(1)
            return tweet_response_body["creation_date"]
        elif detail == "text":
            time.sleep(1)
            return tweet_response_body["text"]
        elif detail == "user_id":
            time.sleep(1)
            return tweet_response_body["96479162"]

    def get_follower_response(self, detail):
        followers = APIFollowers(self.api_request)
        followers_obj = followers.get_followers(self.followers_user_id)
        followers_body = followers_obj.json()
        followers_results = followers_body["results"]
        follower_response_body = followers_results[0]
        if detail == "follower_id":
            time.sleep(1)
            return follower_response_body["user_id"]
        elif detail == "followed_user_id":
            time.sleep(1)
            return self.config["followers_user_id"]
