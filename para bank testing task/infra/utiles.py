import random
import string


class Utiles:

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_phone_number(length):
        letters = string.digits
        return ''.join(random.choice(letters) for _ in range(length))
