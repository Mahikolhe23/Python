def fib(n):
    a = 0 
    b = 1
    c = a + b
    for x in range(1,n):
        print(c)
        a = b
        b = c
        c = a + b
    
fib(int(input("enter number")))

