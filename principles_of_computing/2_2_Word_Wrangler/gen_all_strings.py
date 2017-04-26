


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

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







def test_code():
    '''
    test code
    '''

    print '\n\n', gen_all_strings("aab")

    print '\n\n\n\n\nExpect ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"]'

  
    #word = "at"
    #ans = []
    #for index in range(len(word) + 1):
    #    ans.append(list(gen_ppermutations(word, index)))
    #print ans 

    #print permut("cat")



test_code()





