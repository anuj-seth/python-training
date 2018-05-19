#!/usr/bin/env python

def test_use_format_to_interpolate_variables():
    value1 = 'one'
    value2 = 2
    string = "The values are {0} and {1}".format(value1, value2)
    assert(__ == string)

def test_formatted_values_can_be_shown_in_any_order_or_be_repeated():
    value1 = 'dot'
    value2 = 'DASH'
    string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
    assert(__ == string)

def test_any_python_expression_may_be_interpolated():
    import math  # import a standard python module with math functions
    
    decimal_places = 4
    string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), decimal_places)
    assert(__ == string)

def test_you_can_get_a_substring_from_a_string():
    string = "Arjun, Alia and Sidharth"
    assert(__ == string[7:10])

def test_you_can_get_a_single_character_from_a_string():
    string = "Salman Khan"
    assert(__ == string[1])

def test_single_characters_can_be_represented_by_integers():
    assert(__ == ord('a'))
    assert(__ == ord('b') == (ord('a') + 1))

def test_strings_can_be_split():
    string = "Amar Akbar Anthony"
    words = string.split()
    assert([__, __, __] == words)

def test_raw_strings_do_not_interpret_escape_characters():
    string = r'\n'
    assert('\n' != string)
    assert(__ == string)
    assert(__ == len(string))
    
    # Useful in regular expressions, file paths, URLs, etc.

def test_strings_can_be_joined():
    words = ["Now", "is", "the", "time"]
    assert(__ == ' '.join(words))

def test_strings_can_change_case():
    assert(__ == 'guido'.capitalize())
    assert(__ == 'guido'.upper())
    assert(__ == 'TimBot'.lower())
    assert(__ == 'guido van rossum'.title())
    assert(__ == 'ToTaLlY aWeSoMe'.swapcase())
