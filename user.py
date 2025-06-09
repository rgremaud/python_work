class User:
    """ Create users for ur site """
    def __init__(self, first_name, last_name, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.login_attempts = 0
        self.privileges = Privileges()
    
    def summary(self):
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

    def greeting(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """ Increment login attempts by 1 each time thsi is called """
        self.login_attempts += 1
    
    def total_logins(self):
        print(f"You have logged in {self.login_attempts} times")

    def reset_login_attempts(self):
        """ Reset total login attempts to 0 """
        self.login_attempts = 0


class Admin(User):
    """Adminstrator class for users"""
    def __init__(self, first_name, last_name, height, weight):
        super().__init__(first_name, last_name, height, weight)
        self.privileges = Privileges()

class Privileges():
    """Store user privileges"""
    def __init__(self, privileges = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        print("User privileges:")
        for item in self.privileges:
            print(f"\t- {item}")

new_admin = Admin(first_name = "Whit", last_name = "Gremaud",
                  height = "5 ft 5 in", weight = '120 lbs')


new_admin.privileges.show_privileges()