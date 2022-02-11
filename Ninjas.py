# NINJAS

import Pets

class Ninja:

    def __init__(self, fn = "BLANK", ln = "BLANK", t = "", pf = "", p = ""):
        self.first_name = fn
        self.last_name = ln
        self.pet = p
        self.pet_food = pf
        self.treats = t

####################################

RobyNinja = Ninja("Roby", "Daniele", "Croutons", "ShittyFood", "Cat")

print()

print(RobyNinja.first_name)

