def improve_mood_based_on_list(incomingmood, listofanimals, conditioncap: int):
    """

    :param incomingmood: the current mood we are investigating

    :param listofanimals: list of animals that are monitored

    :param conditioncap: sets the condition criteria
    :type conditioncap: int

    :return: a mood value that is affected by( or not) the condition. variable: newmood
    """
    availablemoods = ['s', 'a', 'h']
    newmood = incomingmood
    criteriafulfilled = [p for p in listofanimals if int(p['Health']) < conditioncap]
    if len(criteriafulfilled) == 0 and incomingmood != 'h':
        newmood = availablemoods[availablemoods.index(incomingmood) + 1]
    return newmood
