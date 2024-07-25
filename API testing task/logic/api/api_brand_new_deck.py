from infra.api.api_wrapper import APIWrapper


class APIBrandNewDeck:

    def __init__(self, request: APIWrapper):
        self._request = request

    def get_brand_new_deck(self, url, is_joker):
        url = f"{url}/new/"
        if is_joker:
            url += "?jokers_enabled=true"
        return self._request.get_request(url)
