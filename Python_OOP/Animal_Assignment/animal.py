
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

    def display_info(self):
        print "Name:", self.name
        print "Health:", self.health
        return self

class Dog(Animal):
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        print "I am a Dragon"
        return self





AnimalCracker = Animal("Mammel", 100)
AnimalCracker.display_info().walk().walk().walk().run().run().display_health()

Lola = Dog("Lola", 150)
Lola.display_info().walk().walk().walk().run().run().pet().display_health()

Drogon = Dragon("Drogon",170)
Drogon.display_info().fly().display_health()