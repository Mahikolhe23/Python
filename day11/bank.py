from customer import Customer


customers = []
for user in range(0,10):
    new_customer = Customer(f'mahi{user}',user,f'pune',user+user)
    customers.append(new_customer)

for user in customers:
    print(user.get_details())

