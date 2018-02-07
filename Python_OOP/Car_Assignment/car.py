class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    #In your __init__(), call this display_all() method 
    #to display information about the car 
    #once the attributes have been defined.

    
    def display_all(self):
    #returns all the information about the car as a string 
        print "Price:", self.price
        print "Speed:", self.speed
        print "Tank:", self.fuel
        print "Milage:", self.milage
        print "Tax:", self.tax
        return self

    
Acura = Car(15000, "200 mph", "Empty" ,"40 mpg")
BMW = Car(20000,"350 mph", "Not Full", "35 mpg" )
Chevrolet = Car(10000, "180 mph", "Full", "40 mpg")
Dodge = Car(8000, "100 mpg", "Not Full", "30 mpg"  )
Ford = Car(2000, "187 mph", "Empty" , "30 mpg")
GMC = Car(7000, "150 mph", "Kind of Full", "25 mpg")

    #If the price is greater than 10,000, set the tax to be 15%.
    #Otherwise, set the tax to be 12%. 

