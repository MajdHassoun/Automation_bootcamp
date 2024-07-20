from infra.api.api_wrapper import APIWrapper


class APITweetReplies:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_tweet_replies(self, url, headers, tweet_id):
        url = f"{url}/tweet/replies?tweet_id={tweet_id}"
        return self._request.get_request(url, headers=headers)
