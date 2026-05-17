class Bank:
    def __init__(self):
        self.balance = 5000
        
b = Bank()
b.balance = -10000  #this one is invalid value
print(b.balance)