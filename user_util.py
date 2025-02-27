import re
import random
import datetime


class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.date.today().year)[2:]
        random_digits = "".join(str(random.randint(0, 9)) for _ in range(7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        while True:
            password = "".join(random.choices(chars, k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()" for c in password))

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$"
        return bool(re.match(pattern, email))