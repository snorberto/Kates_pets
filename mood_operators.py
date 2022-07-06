def improve_mood_based_on_petlist_condition(incomingmood, listofanimals, conditioncap: int):
    """

    :param incomingmood: the current mood we are investigating

    :param listofanimals: list of animals that are monitored

    :param conditioncap: sets the condition criteria
    :type conditioncap: int

    :return: a mood value that is affected by( or not) the condition. variable: newmood
    """
    availablemoods = ['s', 'a', 'h']
    newmood = incomingmood
    if any(int(animal.health) > conditioncap for animal in listofanimals) and incomingmood != 'h':
        newmood = availablemoods[availablemoods.index(incomingmood) + 1]
    return newmood
