def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet                  #"ABC" + "ABC" = "ABCABC"
    return doubleAlphabet


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
# Take three arguments: the message, the cipherKey, and the alphabet.
# Initialize variables.
# Use a for loop to traverse each letter in the message.
# For a specific letter, find the position.
# For a specific letter, determine the new position given the cipher key.
# If current letter is in the alphabet, append the new letter to the encrypted message.
# If current letter is not in the alphabet, append the current letter.
# Return the encrypted message after exhausting all the letters in the message.

def encryptMessage(message, cipherKey, alphabet):               #("hi this is naseer","1","ABCDEFGHIJKLMNOPQRSTUVWXYZ")                   
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()                              #uppercaseMessage= "HI THIS IS NASEER"
    for currentCharacter in uppercaseMessage:                      #  for ' ' in "HI THIS IS NASEER"
        position = alphabet.find(currentCharacter)                  # postion = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find('H')= 7
        newPosition = position + int(cipherKey)                     # newPostion= 7+int("1")= 7+1= 8
        if currentCharacter in alphabet:                                 # if ' '  in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" = False
            encryptedMessage = encryptedMessage + alphabet[newPosition]  # ecrtyptedmessage= "" + alphabet[8] = ""+I   #   ectyptedmessage="IJ"  
        else:
            encryptedMessage = encryptedMessage + currentCharacter      # encryptedmessage="IJ"+" "
    return encryptedMessage

msg=getMessage()                                        #hi this is naseer
key=getCipherKey()                                      #"1"
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciper_output=encryptMessage(msg, key, letters)

print(ciper_output)

# y=getMessage()
# print(y)  
# x="ABC"
# z=getDoubleAlphabet(x)

# print(z)