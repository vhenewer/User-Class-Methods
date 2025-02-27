import unittest
from user_util import UserUtil
import datetime


class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(str(user_id).startswith(str(datetime.date.today().year)[2:]))

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("invalid-email"))

        if __name__ == "__main__":
            unittest.main()
