import random

name = input('enter you name -')
char = int(input('enter digit want in password'))
l1 = len(name)
arr = []
for n in range(0,l1):
    arr.append(name[n])

for n in range(0,char):
    arr.append(random.randint(0,9))

print(arr)
random.shuffle(arr)
print(arr)
