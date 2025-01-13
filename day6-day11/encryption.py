alphabets = []
for i in range(97,123):
    alphabets.append(chr(i))

def encrypt(message , shift):
    new_message = ''
    for letter in message:
        new_shift = alphabets.index(letter) + shift
        if new_shift > 25:
            new_shift = new_shift % len(alphabets)
        new_message += alphabets[new_shift]
    print(new_message)

def decrypt(message , shift):
    new_message = ''
    for letter in message:
        new_shift = alphabets.index(letter) - shift
        if new_shift > 25:
            new_shift = new_shift % len(alphabets)
        new_message += alphabets[new_shift]
    print(new_message)

def welcome():
    coder = str(input('Welcome to coder life\nWhat do you want to do \n1. Encrypt\n2. Decrypt\n')).lower()
    message = input(f'Enter message want to {coder}\n')
    shift = int(input('how many shift do you need\n'))
    if coder == 'encrypt':
        encrypt(message,shift)
    else:
        decrypt(message,shift)    

welcome()



    



 

