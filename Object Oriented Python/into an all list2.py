class Item:
    pay_rate = 0.8 

    all = [] #all list will add all objects that we have to a list 
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
        
        # assign to self object
        self.name = name 
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self): 
        return self.price * self.quantity 

    def apply_discount(self):
        self.price = self.price * self.pay_rate 

    def __repr__(self): #so that we can get a much cleaner & easier to read list for what's in the Item class. 
        # returns [Item("Phone", 100, 2), Item("Laptop", 1000, 3), Item("Cable", 10, 5), Item("Mouse", 50, 5), Item("Keyboard", 75, 5)]
        return f'Item("{self.name}", {self.price}, {self.quantity})'

item1 = Item('Phone', 100, 2)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

print(Item.all)
#for instance in Item.all: #can print the names for all of the instances in the Item.all class. 
    #print(instance.name)


