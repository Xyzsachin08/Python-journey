class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

# Creating objects
m1 = Mobile("Samsung", 20000)
m2 = Mobile("iPhone", 80000)

m1.display()
m2.display()