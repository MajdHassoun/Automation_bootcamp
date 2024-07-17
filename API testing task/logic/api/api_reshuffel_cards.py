from infra.api.api_wrapper import APIWrapper


class APIReshuffelCards:
    def __init__(self, request: APIWrapper):
        self._request = request

    def get_reshuffel_cards(self, url, deck_id, remaining=False):
        url = f"{url}{deck_id}/shuffle"
        if remaining:
            url += "/?remaining=true"
        return self._request.get_request(url)
