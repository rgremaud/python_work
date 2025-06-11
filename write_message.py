from pathlib import Path

gather_names = True
names = ""

while gather_names == True:
    name = input("Please enter your name.  Enter Q to stop. ")
    if name != "Q":
        names += f"{name}\n"
    else:
        break

path = Path('programming.txt')
path.write_text(names)