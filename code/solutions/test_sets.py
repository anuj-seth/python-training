def test_sets_make_keep_lists_unique():
    planets = ['Earth', 'Jupiter', 'Saturn', 'Pluto',
              'Earth', 'Mars', 'Pluto']

    there_can_only_be_only_one = set(planets)

    assert(set(['Mars', 'Earth', 'Saturn', 'Jupiter', 'Pluto']) == there_can_only_be_only_one)

def test_sets_are_unordered():
    assert(set(['1', '3', '4', '5', '2']) == set('12345'))

def test_convert_the_set_into_a_list_to_sort_it():
    assert(['1', '2', '3', '4', '5'] == sorted(set('13245')))

def test_we_can_query_set_membership():
    assert(True == (127 in set([127, 0, 0, 1])))
    assert(True == ('cow' not in set('apocalypse now')))

def test_we_can_compare_subsets():
    assert(True == set('cake').issubset(set('cherry cake')))

