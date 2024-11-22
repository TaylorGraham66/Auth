userList = []

def addParam(param):
    userList.append(param)

def checkList(check):
    if checkUser(userInpt):
        userList = 

while True:
    print("Set your username")
    user = input()
    #Check if username is taken already
    if checkUser(user) == True:
        print('Username is taken, please choose another\n')
        continue
    else:
        break
addParam(user)

#Set password
print("Set your password")
encrPass = Encrypt(input())
addParam(encrPass)

#MFA Setup
print('Pick your security question:')
print("1. " + questionList[0] + " 2. " + questionList[1])
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

#Print the list to the file
toFile(userList)