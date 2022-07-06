import Animal
from Animal import Pet

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
            listofallpets.append(petfromfile)
    moodchain = f.readline()

for mood in moodchain:
    mood = Animal.improve_mood_based_on_list(mood, listofallpets)

    for p in listofallpets:
        pet = Pet(animaltype=p['Type'], animalname=p['Name'], animalhealth=p['Health'])


