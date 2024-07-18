from infra.api.api_wrapper import APIWrapper


class APIUsersLikes:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_users_likes(self, url, headers, limit, user_id):

        url = f"{url}/user/likes?user_id={user_id}&limit={limit}"
        return self._request.get_request(url, headers=headers)
