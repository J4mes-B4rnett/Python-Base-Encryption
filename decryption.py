import math
import time
import os
import json
from math import pow
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

#Python Basic File Decryption
#Made by @Slurp1e

#Requests user target file
target_file = str(input("Target File To Decrypt: "))

#Set the variable to the encrypted file
encrypted_data = open(target_file, "r")
encrypted_data = encrypted_data.read()

def readStringLength(string):
    outputValue = len(string)
    return outputValue

with open('textValues.json', 'r') as json_file:
    alphabetValues = json.load(json_file)

#Reverse Filters

#Filter 1
for i in range(len(encrypted_data)):
    pow(encrypted_data[i], 2)
    print(encrypted_data)