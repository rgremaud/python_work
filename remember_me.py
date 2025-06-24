from pathlib import Path
import json

def get_stored_userinfo(path):
    """Load stored userinfo"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_info(path):
    """Prompt for a new userinfo."""
    username = input("What is your name? ")
    age = input("What is your age? ")
    gender = input("What is your gender? ")
    user_info = {}
    user_info['username'] = username
    user_info['age'] = age
    user_info['gender'] = gender
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def check_user(user_info):
    print(f"Is your username {user_info['username']}?")
    answer = input("Please enter Y or N: ")
    if answer == "Y":
        print(f"Welcome back, {user_info['username']}!")
        print("Profile details:")
        print(f"\tusername: {user_info['username']}")
        print(f"\tage: {user_info['age']}")
        print(f"\tgender: {user_info['gender']}")
    else:
        path = Path('username.json')
        user_info = get_stored_userinfo(path)
        user_info = get_info(path)

    

def greet_user():
    """Greet a user"""
    path = Path('username.json')
    user_info = get_stored_userinfo(path)
    if user_info:
        check_user(user_info)
    else:
        user_info = get_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")

greet_user()

