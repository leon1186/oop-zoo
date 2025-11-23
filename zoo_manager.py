class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Generic Animal Noise"

animaltest1 = Animal("slippy", "Mammal")
print(animaltest1.name)
print(animaltest1.species)
print(animaltest1.speak())

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, "Mammal")

    def give_birth(self):
        print("The Mammal type Animal has given birth")

class Bird(Animal):
    def __init__(self, name, wingspan=1): #wingspan defaulted to 1 to change to null ?
        super().__init__(name, "Bird")
        self.wingspan = wingspan
        print(f"The wingspan of the {self.name} is {self.wingspan} meters")

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name, "Reptile")
    
    def bask_in_sun(self):
        print("This reptile is basking in the sun")

class Bat(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
    def bat_call(self):
        print("Hey Im a Bat using Sonar!!")

class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
    def platypus_sound(self):
        print("Hey Im a Platypus and I make this noise!!")

class Primate(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def climb_trees(self):
        print("The primate is climbing a tree")

class Marsupial(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
    def carry_baby(self):
        print("The Marsupial is carrying its baby")



class Aviary:
    def __init__(self):
        self.birds = []

    def add_bird(self, bird): #type hint? bird: Bird?
       self.birds.append(bird)
    
bird1 = Bird("Pigeon", 0.3)
bird2 = Bird("Eagle", 2.0)
aviary = Aviary()
aviary.add_bird(bird1)
aviary.add_bird(bird2)

print(bird1.name, bird1.wingspan)
print(bird2.name, bird2.wingspan)

print([bird.name for bird in aviary.birds], [bird.wingspan for bird in aviary.birds])


class ReptileEnclosure:
    def __init__(self):
        self.reptiles = []

    def add_reptile(self, reptile): #type hint??? -- bird: Bird
        self.reptiles.append(reptile)


reptile1 = Reptile("Dragon")
reptile2 = Reptile("Iguana")
reptile3 = Reptile("Viper")

reptile_area = ReptileEnclosure()
reptile_area.add_reptile(reptile1)
reptile_area.add_reptile(reptile2)
reptile_area.add_reptile(reptile3)

print([reptile.name for reptile in reptile_area.reptiles])