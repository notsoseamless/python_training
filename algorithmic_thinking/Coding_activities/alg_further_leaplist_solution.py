"""
Solutions for "Recursion: Leap lists" for Further activities
"""


# Exercise 2
def is_goal_reachable_max(leap_list, start_index, max_leaps):
    """ 
    Determines whether goal can be reached in at most max_leaps leaps.

    Arguments:
    leap_list - the leap list game board.
    start_index - the starting index of the player.
    max_leaps - the most number of leaps allowed before the player loses.

    Returns:
    True if goal is reachable in max_leap or less leaps.  False if goal is not reachable in max_leap or fewer leaps.
    """

    if start_index < 0:  # leapt off the list left
        return False
    elif start_index >= len(leap_list):  # leapt off the list right
        return False
    elif leap_list[start_index] == 0:
        return True
    elif max_leaps == 0:
        return False
    else:
        leap_left_index  = start_index - leap_list[start_index]
        leap_right_index = start_index + leap_list[start_index]
        return (is_goal_reachable_max(leap_list, leap_left_index,  max_leaps-1) 
                or is_goal_reachable_max(leap_list, leap_right_index, max_leaps-1))


# Exercise 4
# To solve this problem, you need to keep track of indices that have already been visited. However, you should not change the interface to the function, as "users" of the function do not need to be exposed to such implementation details (they won't know what the parameter is for, what it should be initialized to, etc.). The standard method of dealing with this situation is to define a helper function for internal use only.

def is_goal_reachable(leap_list, start_index):
    """ 
    Determines whether goal can be reached in any number of leaps.

    Arguments:
    leap_list - the leap list game board.
    start_index - the starting index of the player.

    Returns:
    True if goal is reachable.  False if goal is not reachable.
    """
    considered_indices = set()
    return is_goal_reachable_helper(leap_list, start_index, considered_indices)

def is_goal_reachable_helper(leap_list, start_index, considered_indices):
    """ 
    Determines whether goal can be reached in any number of leaps.

    Arguments:
    leap_list - the leap list game board.
    start_index - the starting index of the player.
    considered_indices - a set of positions that should not be explored.

    Returns:
    True if goal is reachable.  False if goal is not reachable.
    """
    if start_index < 0:  # leapt off the list left
        return False
    elif start_index >= len(leap_list):  # leapt off the list right
        return False
    elif leap_list[start_index] == 0:
        return True
    elif start_index in considered_indices:
        return False
    else:
        leap_left_index  = start_index - leap_list[start_index]
        leap_right_index = start_index + leap_list[start_index]
        considered_indices.add(start_index)
        return (is_goal_reachable_helper(leap_list, leap_left_index,  considered_indices) 
                or is_goal_reachable_helper(leap_list, leap_right_index, considered_indices))

