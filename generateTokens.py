
import string
from random import randint

# Creating a file to write generated tokens into .
generatedTokens = open("tokens.txt", "w")
# number of tokens is 10 million as specified in the task .
numOfTokens = 10000000
# All characters used to generate tokens .
lowerCaseCharacters = string.ascii_lowercase
# Length of token .
tokenLength = 7 


"""
loop over number of tokens we want to generate.
    For every token keep on appending a random index from the lowercase characters
    until the token is complete.
    Then write the token to the file and go to the next line .
"""

for x in range(numOfTokens):
    token = ''
    for i in range(tokenLength):
        token += lowerCaseCharacters[randint(0,25)]
    generatedTokens.write(token)
    if(x != numOfTokens-1):
        generatedTokens.write('\n')

generatedTokens.close()






