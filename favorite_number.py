from pathlib import Path
import json

def get_stored_number(path):
    """Load a stored number"""
    if path.exists():
        contents = path.read_text()
        fav_number = json.loads(contents)
        return fav_number
    else:
        return None

def set_fav_number(path):
    """Prompt for a fav number."""
    fav_number = input("What is your favorite number? ")
    contents = json.dumps(fav_number)
    path.write_text(contents)
    return fav_number

def fav_number():
    """Set or load fav number"""
    path = Path('fav_number.json')
    fav_number = get_stored_number(path)
    if fav_number:
        print(f"Your favorite number is {fav_number}!")
    else:
        fav_number = set_fav_number(path)
        print(f"Your number {fav_number} has been stored!")

fav_number()