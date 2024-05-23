# Caesar cipher is based on moving (in the alphabet) a fixed number of times (according to the key) every letter of a message

# in order to use the cipher on every letter of the message we need to double the alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

print(getDoubleAlphabet('ABC')) # 'ABCABC'

# to get from the user the message to cipher
def getMessage():
    stringToEncrypt = input('Please enter a message to encrypt')
    return stringToEncrypt

# to get from the user the number of positions to move a letter (the cipher key)
# it must be in the range of the number of letter of the alphabet)
def getCipherKey():
    shiftAmount = input('Please enter a key (whole number from 1-25)')
    return shiftAmount


# performs the moving of every letter form the message according to the cipher key
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ''
    uppercaseMessage = ''
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


# performs the opposite operation just making negative the cipher key
def decryptMessage(message, cipherkey, alphabet):
    decryptKey = -1 * int(cipherkey)
    return encryptMessage(message, decryptKey, alphabet)

# main function: calls the other helper functions
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncriptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncriptedMessage}')
    myDecryptedMessage = decryptMessage(myEncriptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()

