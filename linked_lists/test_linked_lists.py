from utils import LinkedListNode, LinkedList
from linked_lists import *


# Class Tests
# Node

def test_node_class_exists():
    assert LinkedListNode


def test_node_instantiation_val():
    payload = 4
    actual = LinkedListNode(payload).val
    expected = 4
    assert expected == actual


def test_node_instantiation_nxt():
    payload = '$$'
    actual = LinkedListNode(payload).nxt
    expected = None
    assert expected == actual


# Singly Linked List
def test_linked_list_class_exists():
    assert LinkedList


def test_linked_list_instantiation():
    assert LinkedList()


def test_linked_list_instantiation_one():
    sll = LinkedList([5])
    actual = sll.head.val
    expected = 5
    assert expected == actual


def test_linked_list_instantiation_two():
    sll = LinkedList([3, 1])
    actual = sll.head.val
    expected = 1
    assert expected == actual


def test_linked_List_instantiation_order():
    nodes = [5, 3, 1]
    sll = LinkedList(nodes)
    order = nodes[::-1]
    actual = repr(sll)
    expected = '<LinkedList: {}>'.format(order)
    assert expected == actual


# 2.1
def test_remove_dups_ht():
    sll = LinkedList([1, 1])
    nsll = remove_dups_ht(sll)
    actual = repr(sll)
    expected = '<LinkedList: [1]>'
    assert expected == actual


def test_remove_dups_ht_one_dup():
    sll = LinkedList([1, 1, 2])
    nsll = remove_dups_ht(sll)
    actual = repr(sll)
    expected = '<LinkedList: [2, 1]>'
    assert expected == actual


def test_remove_dups_ht_double_dup():
    sll = LinkedList([3, 4, 3, 1, 1, 2])
    nsll = remove_dups_ht(sll)
    actual = repr(sll)
    expected = '<LinkedList: [2, 1, 3, 4]>'
    assert expected == actual


# 2.1 Solution 2
def test_remove_dups_scout():
    sll = LinkedList([1,1])
    nsll = remove_dups_scout(sll.head)
    actual = repr(sll)
    expected = '<LinkedList: [1]>'
    assert expected == actual


def test_remove_dups_scout_one_dup():
    sll = LinkedList([1,1,2])
    nsll = remove_dups_scout(sll.head)
    actual = repr(sll)
    expected = '<LinkedList: [2, 1]>'
    assert expected == actual


def test_remove_dups_scout_double_dup():
    sll = LinkedList([3,4,3,1,1,2])
    nsll = remove_dups_scout(sll.head)
    actual = repr(sll)
    expected = '<LinkedList: [2, 1, 3, 4]>'
    assert expected == actual


# 2.2
def test_kth_to_last_last():
    sll = LinkedList([6,7,8,9])
    num = 1
    actual = repr(kth_to_last(sll.head, num))
    expected = '<LinkedListNode: [9]'
    assert expected == actual
