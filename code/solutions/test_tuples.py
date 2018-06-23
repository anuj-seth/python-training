
def test_creating_a_tuple():
    count_of_three = (1, 2, 5)
    assert 5 == count_of_three[2]

def test_tuples_can_only_be_changed_through_replacement():
    count_of_three = (1, 2, 5)

    list_count = list(count_of_three)
    list_count.append("boom")
    count_of_three = tuple(list_count)

    assert (1, 2, 5, "boom") == count_of_three

def test_tuples_of_one_look_peculiar():
    # __class__ is a special variable that gives the class name
    # in the below assert statements only replace the underscores on
    # lhs of the equals sign
    assert int == (1).__class__
    assert tuple == (1,).__class__
    t = "Hello comma!",
    assert tuple == t.__class__

    # Note that it's the trailing comma that's essential to creating a tuple.
    # The parentheses are optional, but do use them for readability

def test_tuple_constructor_can_be_surprising():
    assert ('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!',) == tuple("Surprise!")
    assert ('Surprise!',) == tuple(["Surprise!"])

    # do help("tuple") and try to understand what happened here

def test_creating_empty_tuples():
    assert () == ()
    assert () == tuple()  # Sometimes less confusing

def test_tuples_can_be_embedded():
    lat = (37, 14, 6, 'N')
    lon = (115, 48, 40, 'W')
    place = ('Jhumri Telayia', lat, lon)
    assert ('Jhumri Telayia', (37, 14, 6, 'N'), (115, 48, 40, 'W'),) == place

def test_tuples_are_good_for_representing_records():
    locations = [("Mumbai", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
                 ("Pune", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),]

    locations.append(("Hyderabad", (26, 40, 1, 'N'), (70, 45, 7, 'W')))

    assert 'Hyderabad' == locations[2][0]
    assert 15.56 == locations[0][1][2]
