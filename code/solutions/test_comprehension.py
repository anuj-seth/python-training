
def test_creating_lists_with_list_comprehensions():
    food = ['lamb', 'chicken', 'rajma', 'apple',
            'ladoo']
    
    comprehension = [delicacy.capitalize() for delicacy in food]
    
    assert('Lamb' == comprehension[0])
    assert('Rajma' == comprehension[2])

def test_filtering_lists_with_list_comprehensions():
    food = ['lamb', 'chicken', 'rajma', 'apple',
            'ladoo']

    comprehension = [delicacy for delicacy in food if len(delicacy) > 6]
    
    assert(5 == len(food))
    assert(1 == len(comprehension))
    
def test_unpacking_tuples_in_list_comprehensions():
    list_of_tuples = [(1, 'jack'), (2, 'jill'), (4, 'spam')]
    comprehension = [word * number for number, word in list_of_tuples ]

    assert('jack' == comprehension[0])
    assert(16 == len(comprehension[2]))
    
def test_double_list_comprehension():
    list_of_eggs = ['sunny side up egg', 'fried egg']
    list_of_drinks = ['milk', 'cofee', 'tea']
    
    comprehension = ['{0} and {1}'.format(egg, drink) for egg in list_of_eggs for drink in list_of_drinks]
        
    assert(6 == len(comprehension))
    assert('sunny side up egg and milk' == comprehension[0])

def test_creating_a_set_with_set_comprehension():
    comprehension = {x for x in 'aabbbcccc'}
    
    assert(set('abc') == comprehension)  # rememeber that set members are unique

def test_creating_a_dictionary_with_dictionary_comprehension():
    dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                       'third':'ruthless efficiency', 'fourth':'fanatical devotion',
                       'fifth': None}
    
    dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
    
    assert(False == ('first' in dict_comprehension))
    assert(True == ('FIRST' in dict_comprehension))
    assert(5 == len(dict_of_weapons))
    assert(4 == len(dict_comprehension))
