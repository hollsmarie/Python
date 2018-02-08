class Call(object):
    def __init__(self, uniqueID, callerName, callerPhoneNum, timeOfCall, reasonForCall):
        self.uniqueID = uniqueID
        self.callerName = callerName
        self.callerPhoneNum = callerPhoneNum
        self.timeOfCall = timeOfCall
        self.reasonForCall = reasonForCall
        self.display()

    def display(self):
        print "Caller ID:", self.uniqueID
        print "Caller Name:", self.callerName
        print "Phone Number:", self.callerPhoneNum
        print "Time of Call:", self.timeOfCall
        print "Reason for Call:", self.reasonForCall
        return self



class CallCenter(object):
    def __init__(self, list=[], calls=0):
        self.calls = calls   
        # self.name = name
        # self.phone = phone
        self.list = list 
        # self.add()
        # self.info()   
    
    def add(self, newCall):
        while self.calls < 4:
            self.calls += 1
    
        self.list.append(self.calls)
        return self

    def remove(self,done):
        self.list.pop(0)
        self.calls -= 1
        print "Call answered. Caller queue at:", self.calls 
        return self

    def info(self):
        print "Caller in Queue:", self.name
        print "Caller in Queue Phone #", self.phone
        print "Call list:",self.list
        print "Total Calls:",self.calls
        return self
    
Call1 = Call(1, "Holly Valenty", 1234567890, "9:01 AM", "Needs to chat")
Call2 = Call(2, "Lesley Valenty", 1234567890, "9:09 AM", "Has a complaint")
Call3 = Call(3, "Carly Valenty", 1234567890, "3:15 PM", "Wants a refund")
Call4 = Call(4, "Cecily Valenty", 1234567890, "5:09 PM", "Has a question")

CallCenter1 = CallCenter()


CallCenter1.add(Call1).add(Call2).add(Call3).add(Call4).remove(Call1)