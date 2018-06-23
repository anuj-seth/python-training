
def test_creating_lists():
    empty_list = list()
    assert list == type(empty_list)
    assert 0 == len(empty_list)

def test_list_literals():
    nums = list()
    assert [] == nums

    nums[0:] = [1]
    assert [1] == nums

    nums[1:] = [2]
    assert [1, 2] == nums

    nums.append(333)
    assert [1, 2, 333] == nums

    nums[0] = 666
    assert [666, 2, 333] == nums

def test_accessing_list_elements():
    noms = ['google', 'facebook', 'and', 'twitter']

    assert 'google' == noms[0]
    assert 'twitter' == noms[3]
    assert 'twitter' == noms[-1]
    assert 'facebook' == noms[-3]

def test_slicing_lists():
    noms = ['google', 'facebook', 'and', 'twitter']

    assert ['google'] == noms[0:1]
    assert ['google', 'facebook'] == noms[0:2]
    assert [] == noms[2:2]
    assert ['and', 'twitter'] == noms[2:20]
    assert [] == noms[4:0]
    assert [] == noms[4:100]
    assert [] == noms[5:0]

def test_slicing_to_the_edge():
    noms = ['google', 'facebook', 'and', 'twitter']

    assert ['and', 'twitter'] == noms[2:]
    assert ['google', 'facebook'] == noms[:2]

def test_lists_and_ranges():
    assert list == type(list(range(5)))
    assert [0, 1, 2, 3, 4] == list(range(5))
    assert [5, 6, 7, 8] == list(range(5, 9))

def test_ranges_with_steps():
    assert [5, 4] == list(range(5, 3, -1))
    assert [0, 2, 4, 6] == list(range(0, 8, 2))
    assert [1, 4, 7] == list(range(1, 8, 3))
    assert [5, 1, -3] == list(range(5, -7, -4))
    assert [5, 1, -3, -7] == list(range(5, -8, -4))

def test_insertions():
    top_movies = ['Ted', 'Fly Away Home', 'Jumanji']
    top_movies.insert(2, 'Chennai Express')
    assert ['Ted', 'Fly Away Home', 'Chennai Express', 'Jumanji'] == top_movies

    top_movies.insert(0, 'E.T.')
    assert ['E.T.', 'Ted', 'Fly Away Home', 'Chennai Express', 'Jumanji'] == top_movies

def test_concatenate_lists():
    stack = [10, 20, 30, 40]
    elt = ['last']

    assert [10, 20, 30, 40, 'last'] == (stack + elt)

def test_popping_lists():
    stack = [10, 20, 30, 40]
    stack.append('last')

    assert [10, 20, 30, 40, 'last'] == stack

    popped_value = stack.pop()
    assert 'last' == popped_value
    assert [10, 20, 30, 40] == stack

    popped_value = stack.pop(1)
    assert 20 == popped_value
    assert [10, 30, 40] == stack

    # Notice that there is a "pop" but no "push" in python?

    # Part of the Python philosophy is that there ideally should be one and
    # only one way of doing anything. A 'push' is the same as an 'append'.

