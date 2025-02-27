from user import User
from user_service import UserService
from user_util import UserUtil

if __name__ == "__main__":
    user1 = User(UserUtil.generate_user_id(), "Venera", "Ernisova", "2005-06-10")
    UserService.add_user(user1)
    print(user1.get_details())
    print("Total users:", UserService.get_number())