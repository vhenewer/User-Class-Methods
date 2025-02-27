import datetime
from user_util import UserUtil


class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = UserUtil.generate_email(name, surname, "gmail.com")
        self.password = UserUtil.generate_password()
        self.birthday = birthday

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}"

    def get_age(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.birthday, "%Y-%m-%d").date()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age