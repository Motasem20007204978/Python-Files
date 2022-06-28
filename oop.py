
dic = {
    1:'motsdrm',
    2:'almobayyed'
}

print(max(dic.values()))

print(10/5)#result is float
print(5//2)#result is int
print(pow(5,2.5))#result type is according to inputs

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

hamlet.speak()