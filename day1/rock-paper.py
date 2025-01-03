import random

game = ['rock','paper','sissors']
me = input("Enter the number 0, 1, 2")
com = random.randint(0,2)

print('me - '+me)
print('com - '+str(com))
if int(me)==com:
    print('draw')
elif int(me) > com:
    print("You win")
elif int(me)<com:
    print('you loose')
else:
    print("wrong")

