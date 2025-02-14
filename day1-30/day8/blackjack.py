import  random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
game = True
comp = []
you = []

comp.append(random.choice(cards))
you.append(random.choice(cards))
comp.append(random.choice(cards))
you.append(random.choice(cards))
sum_comp = 0
sum_you = 0
print(comp)
print(you)
while game:
    print(comp)
    print(you)
    for n in range(0,len(comp)):
        sum_comp += comp[n]
    for n in range(0,len((you))):
        sum_you += you[n]
    for n in range(0,len(comp)):
        if n == 11 or n == 10:
            print('comp win')
            game = False
    for n in range(0,len(you)):
        if n == 11 or n == 10:
            print('you win')
            game = False
    if sum_you > 21 :
        for n in range(0,len(you)):
            if n != 11 or n == 11 and sum_you - n > 21:
                print('you loose')
                game = False
            else:
                continue
    elif sum_you < 21:
        ans = str(input('do you want another card\ny\nn\n')).lower()
        if ans == 'y':
            you.append(random.choice(cards))
            continue
        elif sum_comp < 17:
            comp.append(random.choice(cards))
        if sum_comp > 21 :
            print('you win')
            game = False
        if sum_you == sum_comp:
            print('draw')
            game = False
        elif sum_comp < sum_you:
            print('you win')
            game = False
        else:
            print('comp win')
            game = False


