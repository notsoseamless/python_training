"""
Student code for Word Wrangler game
JRO - 27/07/2015
"""

#import math
#import urllib2
#import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates1(list1):
    """
    Eliminate duplicates in a sorted list.
    Returns a new sorted list with the same elements in list1, but
    with no duplicates.    
    """
    inp = list(list1)
    ans = []
    for element in inp:
        if element not in ans:
            ans.append(element)        
    return ans            


def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.
    Returns a new sorted list with the same elements in list1, but
    with no duplicates.    
    """ 
    lst = list(list1)
    if len(lst) < 2:
        return lst    
    else:
        if lst[0] != lst[1]:
            return [lst[0]] + remove_duplicates(lst[1:])
        del lst[1]
        return remove_duplicates(lst)

    
def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.
    Returns a new sorted list containing only elements that are in
    both list1 and list2.
    """
    ans = []
    for list1_element in list1:
        for list2_element in list2:
            if list1_element == list2_element and list1_element not in ans:
                ans.append(list1_element)
    return ans


# Functions to perform merge sort
def merge(list1, list2):
    """
    Merge two sorted lists.
    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.
    """ 
    inp1 = list(list1)
    inp2 = list(list2)
    ans = []
    while len(inp1) > 0 and len(inp2) > 0:
        #print 'compare', list1[0], list2[0]
        if inp1[0] <= inp2[0]:
            ans.append(inp1.pop(0))
        else:
            ans.append(inp2.pop(0))
    if inp1:
        ans += inp1
    else:
        ans += inp2      
    return ans


def merge_sort(list1):
    """
    Sort the elements of list1.    
    Return a new sorted list with the same elements as list1.
    This function should be recursive.
    """
    #print list1
    length_list1 = len(list1)
    if length_list1 <= 1: 
        return list1
    else:
        #mid = int(math.floor(length_list1 / 2))
        mid = length_list1 // 2
        left = list1[ : mid]
        right = list1[mid : ]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge(left, right)


# Function to generate all strings for the word wrangler game



def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.
    
    1) Split the input word into two parts: the first character (first) 
       and the remaining part (rest).
    
    2) Use gen_all_strings to generate all appropriate strings for rest.
       Call this list rest_strings.
    
    3) For each string in rest_strings, generate new strings by inserting 
       the initial character, first, in all possible positions within the string.

    4) Return a list containing the strings in rest_strings as well as the new 
       strings generated in step 3.


    This function should be recursive.
    """
    #print '\ncalled with:', word
    if word == "":
        # base case
        #print 'base case - returning', [word], '\n'
        return [word]
    else:
        # inductive case        
        new_strings = [] 
        result=[]
        # step 1
        first = word[0]
        rest = word[1:]
        #print 'first', first
        #print 'rest', rest    

        #step 2 - recursive step, so calling gen_all_strings on the new, shorter word res
        rest_strings = gen_all_strings(rest)
        #print 'rest_strings', rest_strings
        for string in rest_strings:
            #insert the character into every possible location
            for index in range(len(string)+1):
                new_strings.append(string[:index] + first + string[index:])
        result.extend(new_strings)
        result.extend(rest_strings)

        #print 'new_strings', new_strings
        #print 'returning', result, '\n'
        return result 



    



# Function to load words from a file
def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()


def test_code():
    '''
    test code
    '''
    #words = load_words(WORDFILE)
    #url = codeskulptor.file2url(WORDFILE)
    #netfile = urllib2.urlopen(url)
    #data = netfile.read()
    #print data
    #print type(data)
    
    #list1 = ['ab', 'ds', 'ss', 'ss', 'ss', 'zs']
    #list2 = ['aaa', 'ab', 'tss', 'hj']
    #print 'remove_duplicates from ', list1, ':\n', remove_duplicates(list1)
    
    #print '\n\nintersect', intersect(list1, list2)
    
    #print '\n\nlist1', list1
    #print 'list2', list2
    #print 'merge', merge(list1, list2)

    print 'Expect ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"]'
    print gen_all_strings("aab")
  
    
    
    
test_code()



    
    
    

