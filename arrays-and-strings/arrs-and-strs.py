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


# SOLUTION 2 - IN-PLACE SORT
# Efficiency
# space: O(1)  time: O(2n log n)

def unique_chars2(string):

    l = list(string)
    l.sort()

    for i in range(len(l)-1):
        if l[i] == l[i + 1]:
            return False
    
    return True


"""
1.2
Given 2 strings, determine if one is a permutation of the other

Examples
--------
input: 'listen' 'silent'
output: True

input: 'loot' 'tool'
output: True

input: 'listens' 'silent'
output: False

input: 'loot', 'look'
output: False

"""

# SOLUTION 1 - HASHTABLE
# Efficiency
# space: O(n)  time: O(2n)

def permutuation_ht(str1, str2):

    if len(str1) != len(str2):
      return False
  
    d = {}

    for char in str1:
      if char in d:
        d[char] += 1
      else:
        d[char] = 1
    
    for char in str2:

      if char in d:

        if d[char] > 0:
          d[char] -= 1
        else:
          return False

      else:
        return False

    return True


# SOLUTION 2 - SORT & COMPARE
# Efficiency
# space: O(1)  time: O(6n log n)

def permutuation_ht(str1, str2):

    if len(str1) != len(str2):
      return False
  
    l1 = list(str1)
    l2 = list(str2)

    l1.sort()
    l2.sort()

    for i in range(len(str1)):
      if l1[i] != l2[i]:
        return False
    
    return True


"""
1.3
Write a method to replace all spaces in a string with '%20'.
Assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.

Examples
--------
input: 'Mr John Smith    ' '13'
output: 'Mr%20John%20Smith%20'

"""

# SOLUTION - SHIFT & REPLACE FROM END
# Efficiency
# space: O(n)  time: O(n)

def urlify(string, num):

    string = list(string)
    r = len(string) - 1

    for i in range(num -1, -1, -1):

      if string[i] != ' ':
          string[r] = string[i]
          r -= 1

      else:
          string[r] = '0'
          string[r-1] = '2'
          string[r-2] = '%'
          r -= 3

    return ''.join(string)







if __name__ == "__main__":
    # Tests 1.1
    # string1 = 'string'
    # string2 = 'unique'
    # print(unique_chars1(string1))
    # print(unique_chars1(string1))
    # print(unique_chars2(string2))
    # print(unique_chars2(string2))

    #Tests 1.2
    # string1 = 'listen'
    # string2 = 'silent'
    # string1 = 'loot'
    # string2 = 'tool'
    # string1 = 'listens'
    # string2 = 'silent'
    # string1 = 'loot'
    # string2 = 'look'
    # string1 = 'loot'
    # string2 = 'tools'
    # print(permutuation_ht(string1, string2))

    # Tests 1.3
    # phrase = 'Evy Haan  '
    # phrase = 'a b c    '
    # length = 5
    # print(urlify(phrase, length))
