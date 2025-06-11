from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in contents.splitlines():
    new_line = line.replace('Python', 'Ruby')
    print(new_line)

