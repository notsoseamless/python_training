'''
Cool python snips
'''



'''
Comprehensions:
Count items in a sequence
item_count = [seq.count(item) for item in seq]
'''



def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """    
    ans = set([()])
    for _ in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])    
    for _ in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_all_sequences(outcomes, length):
    '''
    Here's a version with a list comprehension. If the reader is used to 
    seeing list comprehensions, I think this version is more easily understood
    than the supplied function.

    The comprehension boils down to, "For every element in outcomes, append that
    element to every sequence in sequences." If you do this 5 times, you end up 
    with 5-tuples (tuples of length 5) in sequences. If you do it 20 times, you
    get 20-tuples.
    '''
    sequences = set([()])
    for dummy_idx in range(length):
        sequences = set([seq + (out,) for seq in sequences for out in outcomes])
    return sequences



def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    item_count = [seq.count(item) for item in seq]
    print item_count
    return max(item_count)










