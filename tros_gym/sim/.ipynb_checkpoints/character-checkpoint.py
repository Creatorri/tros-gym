import numpy as np

def random_char_data(seed=None):
    """Generate random non-magical human character data with no gifts/flaws by optional seed"""
    from numpy.random import default_rng
    if seed == None:
        rng = default_rng()
    else:
        rng = default_rng(seed)
    ranking = rng.shuffle([1,2,3,5])
    # Race
    race = "Human"
    # Social Class
    soclass = {
        1 : (250,"Landed Nobility"),
        2 : (100,"Landless Nobility"),
        3 : (50,"High Freeman"),
        4 : (15,"Low Freeman"),
        5 : (5,"Peasant"),
        6 : (0,"Slave"),
    }[ranking[0]]
    # Attribute Points
    atpoint = {
        1 : 47,
        2 : 43,
        3 : 39,
        4 : 35,
        5 : 31,
        6 : 27,
    }[ranking[1]]
    # Skill Defaults
    skilldef = {
        1 : (6,6),
        2 : (6,7),
        3 : (7,7),
        4 : (8,8),
        5 : (9,9),
        6 : (9,None),
    }[ranking[2]]
    # Proficiency Points
    profpoint = {
        1 : 14,
        2 : 9,
        3 : 6,
        4 : 4,
        5 : 2,
        6 : 0,
    }[ranking[3]]
    if profpoint > 9:
        profmax = 8
    else:
        profmax = 7
    # Gifts/Flaws
    giflaw = None
    # Attributes
    atts = 2*np.ones(10)
    high = rng.integers(0,10)
    atts[high] = rng.integers(np.ceil(atpoint/10),np.min([7,atpoint-np.sum(atts)])) # min for high must allow space for distribution of all points smaller than it and >2
    while np.sum(atts) < atpoints
        big = atts[high]
        pick = rng.integers(0,10)
        atts[pick] = rng.integers(atts[pick],np.min([7,atpoint-np.sum(atts),big]))
    # Skills
    

class Character(object):
    def __init__(data=None):
        if data == None:
            data = random_char_data()