from pathlib import Path

path = Path("example.txt")
line_list = []

def toFile(var):
    with path.open("a") as f:
        f.write(":".join(str(item) for item in var))
        f.write("\n")

userList = ['Taylor', 'encrypted_password', '0', 'the flash']

toFile(userList)

def correctInfo():
    with path.open('r') as f:
        line = f.readline().strip()
        line_list = line.split(':')
        print(line_list)

correctInfo()