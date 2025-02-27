import unittest
from user import User
import datetime

class TestUser(unittest.TestCase):
    def test_get_age(self):
        user = User(123456789, "John", "Doe", "2000-05-15")
        expected_age = datetime.date.today().year - 2000 - (
                    (datetime.date.today().month, datetime.date.today().day) < (5, 15))
        self.assertEqual(user.get_age(), expected_age)

        if __name__ == "__main__":
            unittest.main()
