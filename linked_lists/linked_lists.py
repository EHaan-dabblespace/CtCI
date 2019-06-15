"""
2.1
Remove duplicates from an unsorted linked lists.
What if a temporary buffer is not allow?
"""

# SOLUTION 1 - HASHTABLE
# EFFICIENCY
# space: O(n)  time: O(n)

def remove_dups_ht(sll):
    d = {}
    c = sll
    l = sll

    while c:

        if c.val in d:
            l.nxt = c.nxt
            c = l.nxt
        else:
            d[c.val] = True
            c = c.nxt
            l = l.nxt
    
    return sll


# SOLUTION 2 - SCOUT
# EFFICIENCY
# space: 0(1)  time: O(n^2)

def remove_dups_scout(sll):
    c = sll

    while c:
        t = c.nxt
        l = c

        while t:

            if t.val != c.val:
                t = t.nxt
                l = l.nxt
            else:
                l.nxt = t.nxt
                t = l.nxt
        c = c.nxt
    
    return sll

"""
2.2
Find the kth to the last element of a singly linked list.
(if k = 1, the last element would be returned)
"""

# SOLUTION - ITERATIVE
# EFFICIENCY
# space: O(1)  time: O(n)

def kth_to_last(sll):
    s = sll

    while k > 0:
        s = s.nxt
        k -= 1

    c = sll

    while s.nxt:
        s = s.nxt
        c = c.nxt

    return c

"""
2.3
Delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle)
of a singly linked list, given only access to that node.
"""

# SOLUTION - COPY & REPLACE
# EFFICIENCY
# space: O(1)  time: O(1)

def delete_mid(node):
    c = node
    t = node.nxt

    if not t.nxt:
        raise Exception('The next node is the last in the list. You cannot delete the last node.')

    c.val = t.val
    c.nxt = t.nxt
