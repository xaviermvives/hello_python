# USING FUNCTIONS TO IMPLEMENT A CAESAR CIPHER
a function is a named section of a program that performs a specific task

- built-in functions in Python (print()...)
- you can use functions provided from others through 'import' statement (import math...)
- custom or used-defined functions

a Caesar cipher: a simple method of encryption
it takes the letters of a message and shifts each letter along the alphabet by a certain number of places

Note: Functions should perform a specific task. Usually, because functions perform a specific task, your functions will also probably be short. 

OTHER
- find()
- To help with debugging and understanding the program, print() statements were added, but they are not strictly necessary for the program to operate correctly

RESUM
MAIN FUNCTION: runCaesarCipherProgram()
-getDoubleAlphabet()
-getMessage()
-getCipher()
-encryptMessage()
-decryptMessage()

ENCRYPT FUNCTION
iterar lletra per lletra del missatge
busca index de la lletra a l'alfabet
suma la clau a l'index = dóna nova lletra
crea un nou string amb la nova lletra
repeteix el procés per a totes les lletres
es crea el missatge xifrat

DECRYPT FUNCTION
converteix a numero negatiu la clau de xifrat (-1 * key)
crida la funció encrypt amb la nova clau

INPUT FUNCTIONS
per a obtenir el missatge a encriptar i la clau (un numero 1 )
amb input()


