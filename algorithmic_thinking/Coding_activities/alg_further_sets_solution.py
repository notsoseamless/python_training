"""
Solutions for "Sets" in Further Activities
"""


#Exercise 2 - Union

def union(set1, set2):
    """
    Returns the union of two sets.

    Arguments:
    set1 -- The first set of the union.
    set2 -- The second set of the union.

    Returns:
    A new set containing all the elements of set1 and set2.
    """
    result = set()

    for element in set1:
        result.add(element)

    for element in set2:
        result.add(element)

    return result


#Exercise 3 - Intersection

def intersection(set1, set2):
    """
    Returns the intersection of two sets.

    Arguments:
    set1 -- The first set of the intersection.
    set2 -- The second set of the intersection.

    Returns:
    A new set containing only the elements common to set1 and set2.
    """
    result = set()

    for element in set1:
        if element in set2:
            result.add(element)

    return result

