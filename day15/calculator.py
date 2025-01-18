def cal(n1,n2,func):
    if func == '+':
        return n1 + n2
    if func == '-':
        return n1 - n2
    if func == '*':
        return n1 * n2
    if func == '/':
        if n1 == 0 or n2 == 0:
            print('cant divide to zero or devide by zero')
            return        
    return n1/n2

n1 = int(input('Enter first number\n'))
n2 = int(input('Enter second number\n'))
op = str(input('Enter the operation want to perform\n'))
print(f'Result : {cal(n1=n1,n2=n2,func=op)}')

