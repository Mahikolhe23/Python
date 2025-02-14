class Customer:
    def __init__(self,name,mobile,address,balance):
        self.name = name
        self.mobile = mobile
        self.address = address
        self.balance = balance

    def get_details(self):
        return f'{self.name} {self.mobile} {self.address} {self.balance}'
            


