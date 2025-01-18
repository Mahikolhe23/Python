true = ['t','r','u','e']
love = ['l','o','v','e']
def match(name1, name2):
    name1 = str(name1).lower()
    name2 = str(name2).lower()
    name = name1 + name2
    count1 = 0
    count2 = 0
    for letter in name:
        if letter in true:
            count1 += 1
        if letter in love:
            count2 += 1    
    if count1 == count2:
        print('TURU LOVES')
    else:
        print('Love - ' + str(count1) + str(count2))

name1 = input('Enter first name')
name2 = input('Enter second name')
match(name1=name1,name2=name2)


