def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n/2+1)):
        if n % i == 0 :
            return False
    return True    

number = int(input('Enter the number to check prime'))

if is_prime(number):
    print('This is prime')
else:
    print('This is not prime')
