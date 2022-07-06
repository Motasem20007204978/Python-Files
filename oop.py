
teams = ['Draons', 'Vowels', 'Arjentein', 'Barcelona', 'Madrid']
for team in teams:
    for teamx in list(set(teams)-set(team)):
        print(f"{team} VS {teamx}")


def change_domain(email:str, old_domain:str, new_domain:str)->str:
    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index+1] + new_domain
    return new_email

print(change_domain('motasem@gmail.com', 'gmail.com', 'django.ps'))


class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.sound} I’m {self.name}! {self.sound} ")

class Piglet(Animal):
    sound = "Oink"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "moooo"

cow = Cow("Cow")
cow.speak()

# to shorten the code, we can use it in multiple classes
def decorator(cls):
    class Wrapper:
        def __init__(self, name):
            self.wrapped = cls(name)

        def getName(self):
            return self.wrapped.name

    return Wrapper

@decorator
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
print(p.getName())
        
# inheritanmce and polymorphism 
class GrandFather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername


class Father(GrandFather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        GrandFather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname 
        # encapsulation
        Father.__init__(self, fathername, grandfathername)

    @classmethod 
    def setSon(cls):
        return cls.sonname

    def getSonName(self):
        return self.sonname

    def getGrandFatherName(self):
        return self.grandfathername 
    
    def getFatherName(self):
        return self.fathername

ahmed = Son('motasem', 'anwar', 'khalil')

print(ahmed.getFatherName())
print(ahmed.getGrandFatherName())


