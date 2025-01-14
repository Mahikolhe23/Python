def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return  n1 - n2

def divide(n1,n2):
    return  n1/n2

def multiply(n1,n2):
    return n1 * n2

def cal(n1,n2):
    op = str(input('what do you want to do'))
    if op == '+':
        print(add(n1,n2))
    elif op == '-':
        print(subtract(n1,n2))
    elif op == '/':
        print(divide(n1,n2))
    elif op == '*':
        print(multiply(n1,n2))
    else:
        print('wrong operation')

n1 = int(input('enter first value\n'))
n2 = int(input('enter second value\n'))

cal(n1,n2)
