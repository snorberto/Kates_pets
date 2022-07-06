from mood_operators import improve_mood_based_on_petlist_condition
from Animal import Tarantula, Cat, Hamster


def return_indices_of_pets_with_max_health(incominglist):
    """

    :param incominglist: list from which we select the max elements based on health attribute
    :return: list of indices []
    """
    maxval = None
    indices = []
    for index, val in enumerate(incominglist):
        if maxval is None or int(val.health) > maxval:
            indices = [index]
            maxval = int(val.health)
        elif int(val.health) == maxval:
            indices.append(index)
    return indices


listofallpets = []
petattributenames = ['Type', 'Name', 'Health']

with open("TestFile.txt") as f:
    numberofpets = f.readline()
    if numberofpets != 0:
        for x in range(0, int(numberofpets)):
            getlinefromfile = f.readline().split()
            petfromfile = dict(zip(petattributenames, getlinefromfile))
            if petfromfile['Type'] == 'T':
                listofallpets.append(
                    Tarantula(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                              animalhealth=int(petfromfile['Health']))
                )
            elif petfromfile['Type'] == 'H':
                listofallpets.append(
                    Hamster(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                            animalhealth=int(petfromfile['Health']))
                )
            elif petfromfile['Type'] == 'C':
                listofallpets.append(
                    Cat(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                        animalhealth=int(petfromfile['Health']))
                )

    moodchain = f.readline()

for mood in moodchain:
    mood = improve_mood_based_on_petlist_condition(incomingmood=str.lower(mood), conditioncap=5, listofanimals=listofallpets)
    for pet in listofallpets:
        pet.modify_health_based_on_mood(mood)

    # remove deceased pets:
    listofallpets = [animal for animal in listofallpets if animal.health > 0]

    # if no pets remain alive then exit.
    if len(listofallpets) == 0:
        print("All pets are deceased.")
        break
    # list out animals with the highest health on the given day:
    print("Actual mood cycle: " + mood)
    animalswithhighhealth = list(map(listofallpets.__getitem__, return_indices_of_pets_with_max_health(listofallpets)))
    for animal in animalswithhighhealth:
        print("Animal(s) with highest health: " + animal.name + "|health: " + str(animal.health))
