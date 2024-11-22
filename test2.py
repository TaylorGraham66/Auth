from pathlib import Path
import sys

path = Path("example.txt")
userInpt = ''

def toFile(var):
    with path.open("a") as f:
        f.write(":".join(str(item) for item in var))
        f.write("\n")

#Check if user is correct
def checkUser(inptUser):
    with path.open("r") as f:
        for line in f:
            if inptUser in line:
                return True
        return False

userList = ['Pubert', 'encrypted_password', '0', 'the flash']

toFile(userList)
userInpt = input()

#This function returns the next line, it should return the line it is on
def getList(target_string):
    while True:
        if checkUser(target_string) == True:
            with path.open('r') as f:
                for line in f:
                    if target_string in line:
                        lineCheck = line.strip()
                        line_list = lineCheck.split(':')
                        break
            break
        elif target_string.lower() == 'quit':
            sys.exit()
        elif checkUser(target_string) == False:
            print('That username is not in our system')
            target_string = input()
            continue
    return line_list

line_list = getList(userInpt)
print(line_list)

guess = input()

def checkList(index):
    if guess == line_list[index]:
        return line_list[index]
    else:
        return "That is not in our system"

inList = checkList(0)

if inList == guess:
    print(inList)
else:
    print(inList)