"""
1.1
Implement an algorithm to determine if a string has all unique charactors.
What if you cannot use additional data structures?

Examples
--------
input: 'string'
output: True

input: 'unique'
output: False

"""

# SOLUTION 1 - HASHTABLE
# Efficiency
# space: O(n)  time: O(1)

def unique_chars1(string):

    d = {}

    for char in string:
        if char in d:
            return False
        else:
            d[char] = True
    
    return True

#SOLUTION 2 - IN-PLACE SORT

def unique_chars2(string):

    l = list(string)
    l.sort()

    for i in range(len(l)-1):
        if l[i] == l[i + 1]:
            return False
    
    return True


if __name__ == "__main__":
    string1 = 'string'
    string2 = 'unique'

    print(unique_chars1(string1))
    print(unique_chars1(string1))
    print(unique_chars2(string2))
    print(unique_chars2(string2))
