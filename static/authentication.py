import hashlib
from pathlib import Path
import os
import sys

#Initializing Variables
encrPass = ''
passInpt = ''
path = Path("static\login.txt")
questionList = ['Who is your favorite super hero?', 'What is your moms maiden name?']
question = ''
secAns = ''
userList = []
line_list = []
guess = ''
inList = ''
tries = 3
storedUser = ''


def process_data(data):
    return data['value'] * 2

#Authentication Loop
while True:
    #Encrypt string function
    def Encrypt(string_to_hash):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(string_to_hash.encode('utf-8'))
        hashed_string = sha256_hash.hexdigest()
        return hashed_string

    #Write to file function
    def toFile(var):
        with path.open("a") as f:
            f.write(":".join(str(item) for item in var))
            f.write("\n")

    #Adds the set value to the list
    def addParam(param):
        userList.append(param)

    #Check if user is correct
    def checkUser(inptUser):
        with path.open("r") as f:
            for line in f:
                storedUser = line.split(':')[0]
                if storedUser.lower() == inptUser.lower():
                    return True
            return False
        
    #Checks to see if the user has an account, and if so grabs the list from the database
    def getList(target_string):
        while True:
            if checkUser(target_string) == True:
                with path.open('r') as f:
                    for line in f:
                        stored_user = line.split(":")[0]
                        if stored_user.lower() == target_string.lower():
                            lineCheck = line.strip()
                            line_list = lineCheck.split(':')
                            break
                break
            elif target_string.lower() == 'quit':
                sys.exit()
            elif checkUser(target_string) == False:
                print("Username not recognized. Try again.")
                target_string = input()
                continue
        return line_list
    
    #Checks to see if the value is in the list, and if so returns that value
    def checkList(compare, index):
        if compare == line_list[index]:
            return line_list[index]
        else:
            return "That is not in our system"

    #Checks to see if a special character is in the string
    def hasSpecChar(string):
        return not all(c.isalpha() for c in string)

    #check if login.txt exists
    if not os.path.exists(path):
        f = path.open("x")

    #Check if user already has an account
    print('Do you already have an account? Enter Yes or No')
    skip = input()
    #If no, set up the users account
    if skip.lower() == 'no':
        print('\nNow set up your account')
        #Set username
        while True:
            print("Set your username")
            user = input()
            #Check if username is valid
            if checkUser(user) == True:
                print('Username is taken, please choose another\n')
                continue
            elif user == ' ':
                print('Please enter a valid username')
                continue
            elif user == '':
                print('Please enter a valid username')
            else:
                break
        addParam(user)

        #Set password
        print("Set your password. Special characters are not allowed")
        while True:
            passInpt = input()
            if not hasSpecChar(passInpt): 
                encrPass = Encrypt(passInpt)
                break
            elif passInpt == ' ':
                print('Please enter a valid password')
                continue
            elif passInpt == '':
                print('Please enter a valid password')
            else:
                print('Special Characters are not allowed. Try again')
                continue
        addParam(encrPass)

        #MFA Setup
        print('\nPick one of these to be your security question:')
        print("1. " + questionList[0] + "\n" + "2. " + questionList[1])
        question = input()
        while True:
            if question == "1":
                question = '0'
                addParam(question)
                break
            elif question == "2":
                question = '1'
                addParam(question)
                break
            else:
                print('Invalid input, try again')
                question = input()
        print('Now type your answer to your question.')
        secAns = input()
        addParam(secAns)

        toFile(userList)
        print("You've setup your account! Now login")

    #Else if they do have an account try to login
    elif skip.lower() == 'yes':
            
            #Username login
            print("Please enter your username. Enter 'quit' to stop logging in.")
            while True:
                guess = input()
                line_list = getList(guess)
                inList = checkList(guess, 0)
                break

            #Password Check
            print("Please enter your password. Enter 'quit' to stop logging in.")
            guess = input()
            secAns = Encrypt(guess)
            inList = checkList(secAns, 1)
            while True:
                if inList == secAns:
                    #Password is recognized
                    break
                else:
                    if tries == 1:
                        print("You have 0 tries remaining. You have failed to login")
                        sys.exit()
                    tries -= 1
                    print("Password not recognized. " + str(tries) + " tries remaining.")
                    guess = input()
                    continue

            #MFA Check
            question = line_list[2]
            prntQuest = questionList[int(question)]
            print(prntQuest)
            guess = input()
            inList = checkList(guess, 3)
            while True:
                if inList == guess:
                    #MFA answer is right
                    break
                else:
                    print("MFA Failed")
                    sys.exit()
            break
    else:
        print('Invalid input')
        continue

#Everything was successful
print("You're in!")