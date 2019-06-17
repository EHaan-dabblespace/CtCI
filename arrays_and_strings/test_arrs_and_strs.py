from arrs_and_strs import *

# 1.1


def test_unique_chars1_true():
    input_str = 'string'
    actual = unique_chars1(input_str)
    expected = True
    assert actual == expected


def test_unique_char1_false():
    input_str = 'unique'
    actual = unique_chars1(input_str)
    expected = False
    assert actual == expected


def test_unique_char2_true():
    input_str = 'string'
    actual = unique_chars2(input_str)
    expected = True
    assert actual == expected


def test_unique_char2_false():
    input_str = 'unique'
    actual = unique_chars2(input_str)
    expected = False
    assert actual == expected


# 1.2
def test_permutation_ht_onetoone():
    string1 = 'listen'
    string2 = 'silent'
    actual = permutuation_ht(string1, string2)
    expected = True
    assert actual == expected


def test_permutation_ht_doubledchars():
    string1 = 'loot'
    string2 = 'tool'
    actual = permutuation_ht(string1, string2)
    expected = True
    assert actual == expected


def test_permutation_ht_onedoubledchar():
    string1 = 'listens'
    string2 = 'silent'
    actual = permutuation_ht(string1, string2)
    expected = False
    assert actual == expected


def test_permutation_ht_offbyonediff():
    string1 = 'loot'
    string2 = 'look'
    actual = permutuation_ht(string1, string2)
    expected = False
    assert actual == expected


def test_permutation_ht_offbyoneextra():
    string1 = 'loot'
    string2 = 'tools'
    actual = permutuation_ht(string1, string2)
    expected = False
    assert actual == expected


# 1.3
def test_urilfy_onespace():
    string = 'Evy Haan  '
    length = 8
    actual = urlify(string, length)
    expected = 'Evy%20Haan'
    assert actual == expected


def test_urilfy_twospace():
    string = 'a b c    '
    length = 5
    actual = urlify(string, length)
    expected = 'a%20b%20c'
    assert actual == expected


def test_urilfy_tab():
    string = 'a b  c      '
    length = 6
    actual = urlify(string, length)
    expected = 'a%20b%20%20c'
    assert actual == expected