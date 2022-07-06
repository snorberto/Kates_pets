class Pet(object):
    """
    maximumhealth: defines the animal's maximum health
    moodmodifiers: dict of dict of all the configurations available per animal type and mood.
    """
    maximumhealth = 70
    moodmodifiers = {"s": {"C": -7, "H": -5, "T": -3},
                     "a": {"C": 3, "H": -3, "T": -2},
                     "h": {"C": 3, "H": 2, "T": 1}
                     }

    def __init__(self, animaltype, animalname, animalhealth):
        self.animaltype = animaltype
        self.animalname = animalname
        self.animalhealth = animalhealth

    def modify_health_based_on_mood(self, incomingmood):
        """

        :param incomingmood: the mood that will affect the pet's health
        :return: a modified health for the pet.
        """

        self.animalhealth = str(int(self.animalhealth) + Pet.moodmodifiers[incomingmood][self.animaltype])
