
def test_creating_lists():
    empty_list = list()
    assert(list == type(empty_list))
    assert(__ == len(empty_list))

def test_list_literals():
    nums = list()
    assert([] == nums)
    
    nums[0:] = [1]
    assert([1] == nums)
    
    nums[1:] = [2]
    assert([1, __] == nums)
    
    nums.append(333)
    assert([1, 2, __] == nums)
    
    nums[0] = 666
    assert([__, __, __] == nums)
    
def test_accessing_list_elements():
    noms = ['google', 'facebook', 'and', 'twitter']
    
    assert(__ == noms[0])
    assert(__ == noms[3])
    assert(__ == noms[-1])
    assert(__ == noms[-3])

def test_slicing_lists():
    noms = ['google', 'facebook', 'and', 'twitter']
    
    assert(__ == noms[0:1])
    assert(__ == noms[0:2])
    assert(__ == noms[2:2])
    assert(__ == noms[2:20])
    assert(__ == noms[4:0])
    assert(__ == noms[4:100])
    assert(__ == noms[5:0])

def test_slicing_to_the_edge():
    noms = ['google', 'facebook', 'and', 'twitter']
    
    assert(__ == noms[2:])
    assert(__ == noms[:2])

def test_lists_and_ranges():
    assert(list == type(range(5)))
    assert(__ == range(5))
    assert(__ == range(5, 9))
    
def test_ranges_with_steps():
    assert(__ == range(5, 3, -1))
    assert(__ == range(0, 8, 2))
    assert(__ == range(1, 8, 3))
    assert(__ == range(5, -7, -4))
    assert(__ == range(5, -8, -4))
    
def test_insertions():
    top_movies = ['Ted', 'Fly Away Home', 'Jumanji']
    top_movies.insert(2, 'Chennai Express')
    assert(__ == top_movies)
    
    top_movies.insert(0, 'E.T.')
    assert(__ == top_movies)

def test_concatenate_lists():
    stack = [10, 20, 30, 40]
    elt = ['last']
    
    assert(__ == (stack + elt))

def test_popping_lists():
    stack = [10, 20, 30, 40]
    stack.append('last')
    
    assert(__ == stack)

    popped_value = stack.pop()
    assert(__ == popped_value)
    assert(__ == stack)
    
    popped_value = stack.pop(1)
    assert(__ == popped_value)
    assert(__ == stack)
    
    # Notice that there is a "pop" but no "push" in python?
    
    # Part of the Python philosophy is that there ideally should be one and
    # only one way of doing anything. A 'push' is the same as an 'append'.


    
