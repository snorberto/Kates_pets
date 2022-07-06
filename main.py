from mood_operators import improve_mood_based_on_list
from Animal import Pet, Tarantula, Cat, Hamster

listofallpets = []
petattributenames = ['Type', 'Name', 'Health']
"""
The following segment opens the file which we assume is in the correct format,
then reads all the information into the later used variables within our code.
"""
with open("TestFile.txt") as f:
    numberofpets = f.readline()
    if numberofpets != 0:
        for x in range(0, int(numberofpets)):
            getlinefromfile = f.readline().split()
            petfromfile = dict(zip(petattributenames, getlinefromfile))
            if petfromfile['Type'] == 'T':
                listofallpets.append(
                    Tarantula(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                              animalhealth=petfromfile['Health'])
                )
            elif petfromfile['Type'] == 'H':
                listofallpets.append(
                    Hamster(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                            animalhealth=petfromfile['Health'])
                )
            elif petfromfile['Type'] == 'C':
                listofallpets.append(
                    Cat(animaltype=petfromfile['Type'], animalname=petfromfile['Name'],
                        animalhealth=petfromfile['Health'])
                )

    moodchain = f.readline()

for mood in moodchain:
    mood = improve_mood_based_on_list(incomingmood=str.lower(mood), conditioncap=5, listofanimals=listofallpets)
    for pet in listofallpets:
        pet.modify_health_based_on_mood(mood)

