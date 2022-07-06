from Animal import Pet

allpets = []
petattributenames = ['Type', 'Name', 'Health']

with open("TestFile.txt") as f:
    numberOfPets = f.readline()
    if numberOfPets != 0:
        for x in range(0, int(numberOfPets)):
            getlinefromfile = f.readline().split()
            d = dict(zip(petattributenames, getlinefromfile))
            allpets.append(d)
    moodchain = f.readline()



