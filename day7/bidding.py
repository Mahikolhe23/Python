yes = True
while yes:
    persons_list = {}
    user = str(input("Enter the name of person to bid\n"))
    amount = int(input("Enter the amount want to bid\n"))
    persons_list[user] = amount
    check = str(input("Do you want to other person to bid\nYes\nNO\n")).lower()
    if check == 'yes':
        yes = True
    else:
        yes = False
        final = ''
        max1 = 0
        for key in persons_list:
            if max1 < persons_list[key]:
                max1 = persons_list[key]
                final = key
                print(f'Final bid {max1} by {final}')


