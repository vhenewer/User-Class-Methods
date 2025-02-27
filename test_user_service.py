import unittest
from user import User
from user_service import UserService

class TestUserService(unittest.TestCase):
    def test_add_and_find_user(self):
        user = User(123456789, "Alice", "Smith", "1999-07-21")
        UserService.add_user(user)
        self.assertEqual(UserService.find_user(123456789).name, "Alice")

        if __name__ == "__main__":
            unittest.main()
