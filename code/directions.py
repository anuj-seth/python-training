def string_to_list(directions):
    pass

def read_directions_from_file(file_name):
    pass

def decode_directions(input):
    pass

def test_directions():
    assert 5 == decode_directions(string_to_list('R2, L3'))

    assert 2 == decode_directions(string_to_list('R2, R2, R2'))

    assert 12 == decode_directions(string_to_list('R5, L5, R5, R3'))

    assert 231 == decode_directions(read_directions_from_file('directions.txt'))
