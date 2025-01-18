import  random
print('Welcome to number guess game')
print('Think number between 1 to 100')
num = random.randint(1,100)
level = str(input('choose difficulty level\neasy\nhard\n')).lower()
chance = 0
if level == 'easy':
    chance = 10
else:
    chance = 5

while chance > 0 :
    guess = int(input('Enter the number\n'))
    if guess < num:
        print('too low')
        print(f'only {chance-1} chances is left')
    elif guess > num:
        print('too high')
        print(f'only {chance-1} chances is left')
    elif guess == num:
        print('You won')
        break
    else:
        print('something wrong')
    chance -= 1

if chance == 0 :
    print(f'you loose\nNumber is {num}')