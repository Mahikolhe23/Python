from random import randint, choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','#','$','%','&','*','(',')','+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password_letters = [choice(letters) for _ in range(randint(8,10))]
password_symbols = [choice(symbols) for _ in range(randint(2,4))]
password_numbers = [choice(numbers) for _ in range(randint(2,4))]
password_list = password_letters + password_symbols + password_numbers

shuffle(password_list)

def get_pass():
    password = ''.join(password_list)
    return password
