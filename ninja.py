# NINJAS

import pet


class Ninja:

    def __init__(self, fn="BLANK", ln="BLANK", t="", pf="", p=""):
        self.first_name = fn
        self.last_name = ln
        self.pet = pet.Pet(p)
        self.pet_food = pf
        self.treats = t

    def walk():
        return this

    def feed():
        return this

    def bathe():
        return this

    def myPet(this):
        print(f"MyPet: {this.pet}")
        return this


####################################
RobyNinja = Ninja()

print()
print(RobyNinja.first_name)

################################
RobyNinja.myPet()
