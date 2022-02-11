# NINJAS

from urllib import robotparser
import pet


class Ninja:

    def __init__(self, fn="BLANK", ln="BLANK", t="", pf="", p=""):
        self.first_name = fn
        self.last_name = ln
        self.pet = pet.Pet(p)
        self.pet_food = pf
        self.treats = t

    def walk(this):
        this.pet.play()
        return this

    def feed(this):
        this.pet.eat()
        return this

    def bathe(this):
        this.pet.noise()
        return this

    def getPetName(this):
        print(f"MyPet: {this.pet.name}")
        return this

        	
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method



####################################
RobyNinja = Ninja("Roby", "Daniele", "", "", "Max")

print()
print(RobyNinja.first_name)
print(RobyNinja.last_name)

################################
print()
RobyNinja.getPetName()
print(f"MyPet: {RobyNinja.pet.name}")

print()
RobyNinja.walk()
RobyNinja.bathe()
RobyNinja.feed()

##################

EricNinja = Ninja("Eric", "Niemo", "asdf", "asdf", "Ed_Man")
EricNinja.feed()