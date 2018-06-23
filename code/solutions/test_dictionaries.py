def test_creating_dictionaries():
    empty_dict = dict()
    assert dict == type(empty_dict)
    assert dict() == empty_dict
    assert 0 == len(empty_dict)

def test_dictionary_literals():
    empty_dict = {}
    assert dict == type(empty_dict)
    babel_fish = {'one': 'uno', 'two': 'dos'}
    assert 2 == len(babel_fish)

def test_accessing_dictionaries():
    babel_fish = {'one': 'uno', 'two': 'dos'}
    assert 'uno' == babel_fish['one']
    assert 'dos' == babel_fish['two']

def test_changing_dictionaries():
    babel_fish = {'one': 'uno', 'two': 'dos'}
    babel_fish['one'] = 'eins'

    expected = {'two': 'dos', 'one': 'eins'}
    assert expected == babel_fish

def test_dictionary_is_unordered():
    dict1 = {'one': 'uno', 'two': 'dos'}
    dict2 = {'two': 'dos', 'one': 'uno'}

    assert {'two': 'dos', 'one': 'uno'} == dict1 == dict2

def test_dictionary_keys_and_values():
    babel_fish = {'one': 'uno', 'two': 'dos'}
    assert 2 == len(babel_fish.keys())
    assert 2 == len(babel_fish.values())
    assert True == ('one' in babel_fish.keys())
    assert False == ('two' in babel_fish.values())
    assert False == ('uno' in babel_fish.keys())
    assert True == ('dos' in babel_fish.values())

