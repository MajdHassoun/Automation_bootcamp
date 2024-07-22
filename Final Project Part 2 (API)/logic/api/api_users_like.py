from infra.api.api_wrapper import APIWrapper


class APIUsersLikes:
    """
    The APIUsersLikes class interacts with an API to retrieve tweets liked by a specific user.
    """

    def __init__(self, request: APIWrapper):
        """
        Initializes the APIUsersLikes class with an APIWrapper instance.

        Parameters:
        request (APIWrapper): An instance of the APIWrapper class to handle HTTP requests.
        """
        self._request = request

    def get_users_likes(self, url, headers, limit, user_id):
        """
        Retrieves tweets liked by a user based on the user ID and a specified limit.

        Parameters:
        url (str): The base URL for the API.
        headers (dict): The headers to include in the API request.
        limit (int): The maximum number of liked tweets to retrieve.
        user_id (str): The ID of the user.

        Returns:
        The response from the API request.
        """
        url = f"{url}/user/likes?user_id={user_id}&limit={limit}"
        return self._request.get_request(url, headers=headers)