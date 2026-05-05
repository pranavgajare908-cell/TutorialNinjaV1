import datetime
import random
import uuid


class DataGenerator:
    @staticmethod
    def generate_email():
        chars = "abcdefghijklmnopqrstuvwxyz0123456789!"
        email = "".join(random.choice(chars) for _ in range(10))
        return email + "@gmail.com"
