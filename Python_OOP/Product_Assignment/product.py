class Product(object):
    def __init__(self, price, itemName, weight, brand, status="for sale"):
        self.price = price 
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = status
        self.display()
    

    def sell(self, reason):
        if self.status is True:
            print "Sold"
        elif self.status is False:
            print "For Sale"
        else: 
            giveback(self)
        return self

    def Tax(self,tax):
         sales = self.price * (1+ tax)
         return sales

    def Giveback(self):
        if self.reason is defect:
            print "defective"
            self.price == 0
        elif self.reason is used:
            print "used"
            self.price == self.price * .80
        else:
            print "For Sale"
        return self

    def display(self):
        print "Price:", self.price
        print "Name:", self.itemName
        print "Weight:", self.weight
        print "Made by:", self.brand
        print "Status:", self.status
        return self


product1 = Product(40, "The Prisoner", "750 ml", "The Prisoner Wine Co") .Tax(.07)
product2 = Product(30, "Silver Tequila", "1 L", "El Jimador")
product3 = Product(800, "Pappy Van Winkle", "1 L", "Buffalo Trace")