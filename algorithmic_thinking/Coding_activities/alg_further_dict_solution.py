"""
Solutions for "Dictionaries" in Further activities
"""

# Exercise 1 - Dictionary Creation

def make_dict(keys, default_value):
    """
    Creates a new dictionary with the specified keys and default value.

    Arguments:
    keys          -- A list of keys to be included in the returned dictionary.
    default_value -- The initial mapping value for each key.

    Returns:
    A dictionary where every key is mapped to the given default_value.
    """
    result = { }

    for key in keys:
        result[key] = default_value    
    return result


# Exercise 2 - Value Assertion

def ensure_key_value_pair(pairs, key, expected_value):
    """
    Checks to ensure that the mapping of key in pairs matches the given expected value.

    If the state of pairs is such that the given key is already mapped to the given expected value
    this function performs no action and immediately returns the given dictionary.

    If the state of pairs is such that the given key does not map to the given expected value
    (or no such key is contained in pairs) then update (or add) the mapping of key to
    the given expected value and return the given dictionary.

    Arguments:
    pairs          -- A dictionary to check for the expected mapping.
    key            -- The key of the expected mapping.
    expected_value -- The the value of the expected mapping.

    Returns:
    The given dictionary.
    """
    if pairs.has_key(key):
        found_value = pairs[key]
        if found_value == expected_value:
            return pairs # key was found and mapped to exepcted value
        else:
            pairs[key] = expected_value
            return pairs # key was found and not mapped to exepcted value      
    else:
       pairs[key] = expected_value
       return pairs # given key was not found

