"""Admin and privileges class"""

from user import User

class Admin(User):
    """Adminstrator class for users"""
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()

class Privileges():
    """Store user privileges"""
    def __init__(self, privileges = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print("User privileges:")
        for item in self.privileges:
            print(f"\t- {item}")
