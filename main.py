from mood_operators import improve_mood_based_on_list
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
    print("before change: " + mood)
    mood = improve_mood_based_on_list(incomingmood=str.lower(mood), listofanimals=listofallpets, conditioncap=5)
    print("after change: " + mood)

    for p in listofallpets:
        pet = Pet(animaltype=p['Type'], animalname=p['Name'], animalhealth=p['Health'])
        print("before the change: " + str(pet.animalhealth))
        pet.modify_health_based_on_mood(mood)
        print("after the change: " + str(pet.animalhealth))
