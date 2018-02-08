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
    def __init__(self, name, phone):
        self.calls = 1   
        self.queueSize = 0
        self.name = name
        self.phone = phone
        self.list = [] 
        self.add()
        self.info()   
    
    def add(self):
        while self.calls < 4:
        # for calls in queueSize:
            self.calls += 1
            self.queueSize += 1
        self.list.append(self.calls)
        return self

    def remove(self):
        self.list.pop(0)
        return self

    def info(self):
        print "Caller in Queue:", self.name
        print "Caller in Queue Phone #", self.phone
        print "Queue Size:", self.queueSize
        print "Call list:",self.list
        print "Total Calls:",self.calls
        return self
    
Call1 = Call(1, "Betty Boop", 1234567890, "9:01 AM", "Needs to chat")
CallCenter1 = CallCenter("Holly",55536725555)
CallCenter2 = CallCenter("Lesley",5555555235)
CallCenter3 = CallCenter("Carly",5572755555)
CallCenter4 = CallCenter("Cecily",5522255555)