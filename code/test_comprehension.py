
def test_creating_lists_with_list_comprehensions():
    food = ['lamb', 'chicken', 'rajma', 'apple',
             'ladoo']
    
    comprehension = [delicacy.capitalize() for delicacy in food]
    
    assert(__ == comprehension[0])
    assert(__ == comprehension[2])

def test_filtering_lists_with_list_comprehensions():
    food = ['lamb', 'chicken', 'rajma', 'apple',
            'ladoo']

    comprehension = [delicacy for delicacy in food if len(delicacy) > 6]
    
    assert(__ == len(food))
    assert(__ == len(comprehension))
    
def test_unpacking_tuples_in_list_comprehensions():
    list_of_tuples = [(1, 'jack'), (2, 'jill'), (4, 'spam')]
    comprehension = [word * number for number, word in list_of_tuples ]

    assert(__ == comprehension[0])
    assert(__ == len(comprehension[2]))
    
def test_double_list_comprehension():
    list_of_eggs = ['sunny side up egg', 'fried egg']
    list_of_drinks = ['milk', 'cofee', 'tea']
    
    comprehension = ['{0} and {1}'.format(egg, drink) for egg in list_of_eggs for drink in list_of_drinks]
        
    assert(__ == len(comprehension))
    assert(__ == comprehension[0])

def test_creating_a_set_with_set_comprehension():
    comprehension = {x for x in 'aabbbcccc'}
    
    assert(__ == comprehension)  # rememeber that set members are unique

def test_creating_a_dictionary_with_dictionary_comprehension():
    dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                       'third':'ruthless efficiency', 'fourth':'fanatical devotion',
                       'fifth': None}
    
    dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
    
    assert(__ == ('first' in dict_comprehension))
    assert(__ == ('FIRST' in dict_comprehension))
    assert(__ == len(dict_of_weapons))
    assert(__ == len(dict_comprehension))
