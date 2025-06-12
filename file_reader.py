from pathlib import Path

path = Path('text_files/cats.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"The file {path} is not found")
else: 
    print("\nCat names:\n")
    print(contents)

dog_path = Path('dogs.txt')
try:
    contents = dog_path.read_text()
except FileNotFoundError:
    pass
else: 
    print("\nDog names:\n")
    print(contents)