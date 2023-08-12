from random import choice
import json
import time
import os

# simple password generator and saver
os.system('clear')

charsJson = open('allchars.json', 'r')
chars = json.load(charsJson)

savedPasswordsJson = open('savedpasswords.json', 'r')
savedPasswords = json.load(savedPasswordsJson)

def debugMode(openDebugMode):
    if (openDebugMode == 'Yes'):
        print('Writing all chars....')
        time.sleep(1)
        l = 0
        for p in chars:
            l+=1
            print("Char number " + str(l) + ": " + str(p))
        print("Printed " + str(l) + " chars")
        print("Writing all saved passwords.... ")
        time.sleep(2)
        for m in savedPasswords:
            print(m)
        print("Printed all passwords")
        print("Grabbed from files: allchars.json and savedpasswords.json")
        clearDebug = input("Clear Debug Logs? ")
        if (clearDebug == 'Yes'):
            os.system('clear')


def generateAndSavePasscode(passwordLength, passwordFor, savePassword):
    #passwordLength = int(input("How long should the password be? "))
    #passwordFor = input("What is this password for? ")
    print("Generating a password with a length of: " + str(passwordLength))
    generatedPasscode = ''.join(
        choice(chars) for i in range(passwordLength)
    )
    time.sleep(1)
    print("Generated passcode: " + str(generatedPasscode) + " for " + passwordFor)
    if (savePassword == "Yes"):
        fullGeneratedPasscode = passwordFor + ": " + generatedPasscode
        savedPasswords.append(fullGeneratedPasscode)
        with open('savedpasswords.json', 'w') as outfile:
            json.dump(savedPasswords, outfile)
        time.sleep(1)
        print("Saved passwords")

def printPasswords(writePasswords):
    if (writePasswords == "Yes"):
        for q in savedPasswords:
            print(q)

debugMode(input("Open Debug Mode? "))
generateAndSavePasscode(int(input("How long should the password be? ")), input("What is this password for? "), input("Save Password?(Yes or No)"))
printPasswords(input("Want to write out all passwords?"))