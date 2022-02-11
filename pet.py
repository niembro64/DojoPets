# PETS

class Pet:

    def __init__(self, n="BLANK_PET", ty="", tr="", h="", e=""):
        self.name = n
        self.type = ty
        self.tricks = tr
        self.health = h
        self.energy = e

    def sleep(this):
        print(f"{this.name} is sleeping")
        return this

    def eat(this):
        print(f"{this.name} is eating")
        return this

    def play(this):
        print(f"{this.name} is playing")
        return this

    def noise(this):
        print(f"{this.name} is making a noise")
        return this

####################

class Dog(Pet):

    def __init__ (self, c = "BLANK_COLOR"):
        self.color = c

class Cat(Pet):

    def __init_ (self, c = "BLANK_COLOR"):
        self.collarColor = c