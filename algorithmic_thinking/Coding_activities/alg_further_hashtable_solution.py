"""
Solution to "Hash tables" for Further activities
"""

# Exercise 2
def create_ht(ht_size):
   """ Returns an empty hash table of size ht_size.
 
   Arguments:
   ht_size - the length of the hash table
 
   Returns:
   A hash table containing ht_size empty chains (lists).
   """
   hash_table = []
   for i in xrange(ht_size):
       hash_table.append([])

   return hash_table

 
def add_ht(ht,key,value):
   """
   Adds to key/value pair to the hash table ht.
   If the key is already in the hash table, replace its old value with the new.
 
   Arguments:
   ht - the hash table
   key - the key of the key value pair to store
   value - the value of the key value pair to store
   """
   index = hash(key) % len(ht)
   chain = ht[index]
   
   for kvp in chain:
       e_key = kvp[0]
       e_value = kvp[1]

       if e_key == key:
           chain.remove(kvp)
           break;

   chain.append((key, value))

def contains_key_ht(ht, key):
    """
    Tests whether a given key is contained in a hash table.

    Arguments:
    ht - the hash table
    key - the key to search for within the hash table

    Returns:
    True if the key is found, false otherwise.
    """
    index = hash(key) % len(ht)
    chain = ht[index]

    for kvp in chain:
       e_key = kvp[0]
       e_value = kvp[1]

       if e_key == key:
           return True

    return False
     
def remove_ht(ht, key):
    """
    Removes a key's value from the hash table.
    If no key is found in the table, no action is taken.
    
    Arguments:
    key - the key to search for in the hash table
    """  

    index = hash(key) % len(ht)
    chain = ht[index]
   
    for kvp in chain:
       e_key = kvp[0]
       value = kvp[1]

       if e_key == key:
            chain.remove(kvp)
            return
 
def lookup_ht(ht,key):
   """
   Returns the value associated with the key in the hash table ht.
   If the key is not present, raise an error.
 
   Returns:
   The value associated with the given key.
   """
   index = hash(key) % len(ht)
   chain = ht[index]
   
   for kvp in chain:
       e_key = kvp[0]
       value = kvp[1]

       if e_key == key:
            return value

   raise Exception("No key found in hash table.")

        
def run_hashtable():
    """
    Create a hash table and perform some operations on it
    """
    table = create_ht(1000)
    add_ht(table, "cat", 29)
    print "Table contains 'dog' =", contains_key_ht(table, "dog")
    print "Table contains 'cat' =", contains_key_ht(table, "cat")
    print "The value for 'cat' is", lookup_ht(table, "cat")
    
run_hashtable()
        
    
    
# Exercise 3


import time

def ht_test(n,size):
    """
    Computes search time for the nth element of hash table.

    Arguments:
    n - the number of elemements in the table.
    size - the size of the table

    Returns:
    The lookup time in seconds.
    """

    ht = create_ht(size)

    for i in xrange(n):
        add_ht(ht, i, i)

    start = time.time()
    lookup_ht(ht, n-1)
    stop = time.time()
    return stop - start

def list_test(n):
    """
    Computes search time for the nth element of a list.

    Arguments:
    n - the number of elemements in the list.

    Returns:
    The lookup time in seconds.
    """

    lst = []

    for i in xrange(n):
        lst.append(i)

    start = time.time()
    lst.index(n-1)
    stop = time.time()
    return stop - start


def run_timing():
    """
    Compare speed of list search to hash table lookup
    """
    print "Time for hash table lookup is", ht_test(1000000, 100000)
    print "Time for list search is", list_test(1000000)
    
run_timing()
    
        
# Exercise 4
def rehash_ht(ht, size):
    """
    Rehashes the given hash table in place to a new chain size.

    Arguments:
    ht - the hash table to modify
    size - the new hash table size
    """

    kvps = set()

    while len(ht) > 0:
        chain = ht.pop()
        while len(chain) > 0:
            kvps.add(chain.pop())

    for i in xrange(size):
        ht.append([])

    for kvp in kvps:
        add_ht(ht, kvp[0], kvp[1])
        

