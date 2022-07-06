# parent class:
class Pet(object):
    maxhealth = 70

    def __init__(self, animaltype, animalhealth: int, animalname, sadmood: int, avgmood: int, happymood: int):
        self.type = animaltype
        self.health = animalhealth
        self.name = animalname
        self.sadmood = sadmood
        self.avgmood = avgmood
        self.happymood = happymood

    def modify_health_based_on_mood(self, incomingmood):
        """

        :param incomingmood: char that defines which self attribute to use when modifying health attribute
        :return: self.health attribute changed.
        """
        if incomingmood == 's':
            self.health = int(self.health) + self.sadmood
        elif incomingmood == 'a':
            self.health = int(self.health) + self.avgmood
        elif incomingmood == 'h':
            self.health = int(self.health) + self.happymood

        if self.health > Pet.maxhealth:
            self.health = Pet.maxhealth


# child class
class Cat(Pet):
    def __init__(self, animaltype, animalhealth, animalname, sadmood=-7, avgmood=3, happymood=3):
        Pet.__init__(self, animaltype, animalhealth, animalname, sadmood, avgmood, happymood)


# child class
class Tarantula(Pet):
    def __init__(self, animaltype, animalhealth, animalname, sadmood=-3, avgmood=-2, happymood=1):
        Pet.__init__(self, animaltype, animalhealth, animalname, sadmood, avgmood, happymood)


# child class
class Hamster(Pet):
    def __init__(self, animaltype, animalhealth, animalname, sadmood=-5, avgmood=-3, happymood=2):
        Pet.__init__(self, animaltype, animalhealth, animalname, sadmood, avgmood, happymood)
