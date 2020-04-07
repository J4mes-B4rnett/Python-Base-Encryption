import math
import time
import os
import json

#Python Basic File Encryption & Decryption
#Made by @Slurp1e

option = input("Encryption or Decryption: ")
if option == "Encryption":

    #Requests user target file
    target_file = input("Target File To Encrypt: ")

    #Set the variable to the unencrypted txt
    unencrypted_data = open(target_file, "r")
    unencrypted_data = unencrypted_data.read()

    #Length of targeted string
    def countString(string):
        returnValue = len(string)
        return returnValue

    with open('textValues.json', 'r') as json_file:
        alphabetValues = json.load(json_file)

    stringValues = {}

    filter_1 = []
    #Filter 1

    i = 0
    print("Filter 1")
    while i < countString(unencrypted_data):
        filter_1.append(alphabetValues[unencrypted_data[i]])
        i += 1
        print(filter_1)

    time.sleep(0.5)

    filter_2 = []
    #Filter 2

    i = 0
    print("Filter 2")
    while i < countString(unencrypted_data):
        filter_2.append(filter_1[i] * 3)
        print(filter_2)
        i += 1

    time.sleep(0.5)

    filter_3 = []
    #Filter 3

    i = 0
    print("Filter 3")
    while i < countString(unencrypted_data):
        filter_3.append(math.sqrt(filter_2[i]))
        print(filter_3)
        i += 1

    time.sleep(0.5)

    #Outputting encryption
    print("Outputting File...")
    time.sleep(0.3)
    print("Setting Output String...")
    time.sleep(0.1)
    output = filter_3
    print("Removing Old File...")
    time.sleep(0.5)
    os.remove("ued.txt")

    print("Generating Encryption File...")
    time.sleep(1)
    outputString = str(filter_3)

    outputFile = open(target_file, "w")
    outputFile.write(outputString)

    print("Finished...")

elif option == "Decryption":

    #Requests user target file
    target_file = input("Target File To Decrypt: ")

    #Set the variable to the unencrypted txt
    encrypted_data = open(target_file, "r")
    encrypted_data = encrypted_data.read()

    #Length of targeted string
    def countString(string):
        returnValue = len(string)
        return returnValue

    def Convert(string):
        li = list(string.split("-"))
        return li

    with open('textValues.json', 'r') as json_file:
        alphabetValues = json.load(json_file)

    # Reverse Filters
    # Filter 1
    for i in range(len(encrypted_data)):
        print(Convert(encrypted_data[i]))
