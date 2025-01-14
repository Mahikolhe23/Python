yes = True
customers = {}    
while yes:
    print('Welcome to SBI Bank\nWhat do you want to process\n1.add new customer\n2.update customer\n3.see all customer')
    task_number = int(input('Enter the number of task\n'))
    if task_number == 1:
        name = str(input('Enter the name of customer\n'))
        amount = int(input('Enter the amount want to deposit\n'))
        customers[name] = amount
    elif task_number == 2:
        name = str(input('enter the name of existing customer\n'))
        amount = int(input('Enter the amount want to deposit\n'))
        customers[name]+=amount
    elif task_number == 3:
        print(customers)
    else:
        print('Invalid number')
    other = str(input('do you want anything else\n')).lower
    if other == 'no':
        yes = False
        




