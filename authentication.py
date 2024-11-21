
import hashlib
from pathlib import Path
import os
import sys

#Initializing Variables
encrPass = ''
decrPass = ''
userInpt = ''
passInpt = ''
triedPass = ''
userDone = False
path = Path("login.txt")
questionList = ['Who is your favorite super hero?', 'What is your moms maiden name?']
question = ''
secAns = ''
guessSecAns = ''

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
            f.write(var + "\n")
            f.close()

    #Check if user is correct
    def checkUser(inptUser):
        with path.open("r") as f:
            for line in f:
                if inptUser in line:
                    return True
            return False

    #Read out the next line in the file
    def nextLine(target_string):
        with path.open("r") as f:
            for line in f:
                if target_string in line:
                    return next(f, None).strip()
        return None
    
    def twoLines(target_string2):
        with path.open('r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if target_string2 in line:
                    if i + 2 < len(lines):
                        return lines[i + 2]
                    else:
                        return "Not in file"
        return "Wrong"

    def threeLines(target_string2):
        with path.open('r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if target_string2 in line:
                    if i + 2 < len(lines):
                        return lines[i + 3]
                    else:
                        return "Not in file"
        return "Wrong"

    #check if login.txt exists
    if not os.path.exists(path):
        f = path.open("x")

    #Check if user already has an account
    print('Do you already have an account? Enter Yes or No')
    skip = input()
    #If no, set up the users account
    if skip.lower() == 'no':
        print('\nNow set up your account\n')
        #Set username
        while not userDone:
            print("Set your username")
            user = input()
            #Check if username is taken already
            if checkUser(user) == True:
                print('Username is taken, please choose another\n')
                continue
            else:
                break
        toFile(user)

        #Set password
        print("Set your password")
        decrPass = input()
        encrPass = Encrypt(decrPass)
        toFile(encrPass)

        #MFA Setup
        print('Pick your security question:')
        print("1. " + questionList[0] + " 2. " + questionList[1])
        question = input()
        while True:
            if question == "1":
                question = '0'
                toFile(question)
                break
            elif question == "2":
                question = '1'
                toFile(question)
                break
            else:
                print('Invalid input, try again')
                question = input()
        print('Now type your answer to your question.')
        secAns = input()
        toFile(secAns)


        print("You've setup your account! Now login")

    #Else if they do have an account try to login
    elif skip.lower() == 'yes':
            #Username login
            print('Please enter your username. Type quit to stop logging in.')
            userInpt = input()
            #Quit if needed
            if userInpt.lower() == 'quit':
                break
            while not checkUser(userInpt):
                print("That username is not in our system, try again")
                userInpt = input()

            #For loop to have 3 tries to input the correct password
            for i in range(3):
                if checkUser(userInpt) == True:
                    print("Now enter the password for " + userInpt + ". Type quit to stop logging in.")
                    passInpt = input()
                    if passInpt.lower() == 'quit':
                        break
                    triedPass = Encrypt(passInpt)
                    if nextLine(userInpt) == triedPass:
                        i = 3
                        break
                    else:
                        tries = 2 - i
                        i + 1
                        print('You have ' + str(tries) + ' tries remaining!')
                        if tries == 0:
                            sys.exit
            
            #MFA
            print('Now answer your MFA question.')
            print(questionList[int(twoLines(userInpt))])
            guessSecAns = input()
            print (threeLines(userInpt))
            if guessSecAns.strip().lower() == threeLines(userInpt).strip().lower():
                print('You got it right!')
            else:
                print('You got it wrong! Redo your authentication')
                continue
            break
    
    else:
        print('Invalid input')
        continue

print("You're in!")