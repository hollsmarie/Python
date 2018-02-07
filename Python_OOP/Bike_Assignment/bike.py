class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    
    def ride(self):
        self.miles += 10
        print "Riding", self.miles 
        return self

    def reverse(self):
        if self.miles < 5:
            print "stop reversing"
        else: 
            self.miles -= 5
            print "Reversing", self.miles
        return self

Schwinn = Bike(300, "30 mph")
Blue = Bike(250, "20 mph")
Yamaha = Bike(600, "120 mph")

Schwinn.ride().ride().ride().reverse().displayinfo()
Blue.ride().ride().reverse().reverse().displayinfo()
Yamaha.reverse().reverse().reverse().displayinfo()

#self is always with init function/method 
#return self allows you to chain them together 