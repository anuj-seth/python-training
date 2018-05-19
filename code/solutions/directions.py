def string_to_list(directions):
    return [[directive.strip()[0], int(directive.strip()[1:])] for directive in directions.strip().split(',')]

def read_directions_from_file(file_name):
    with open(file_name) as infile:
        line = infile.readline()
        return string_to_list(line)

def decode_directions_intersect_functional(input):
    rules = {('N', 'R'):['E', [1, 0]],
             ('N', 'L'):['W', [-1, 0]],
             ('S', 'R'):['W', [-1, 0]],
             ('S', 'L'):['E', [1, 0]],
             ('E', 'R'):['S', [0, -1]],
             ('E', 'L'):['N', [0, 1]],
             ('W', 'R'):['N', [0, 1]],
             ('W', 'L'):['S', [0, -1]]}
    starting_point = ['N', (0, 0)]
    current_state = starting_point
    already_seen = set([(0,0)])
    intersect_position = None
    for turn_to, move in input:
        facing, [current_x, current_y] = current_state
        [new_facing, [x_inc, y_inc]] = rules[(facing, turn_to)]
        intermediate_moves = [[x_inc * multiplier, y_inc * multiplier] for multiplier in range(1, move +1)]
        intermediate_positions = [(current_x + x_inc, current_y + y_inc) for [x_inc, y_inc] in intermediate_moves]
        for position in intermediate_positions:
            if position in already_seen:
                intersect_position = position
                break
            else:
                already_seen.add(position)

        if intersect_position:
            break
        current_state = [new_facing, intermediate_positions[-1]]

    return sum([abs(x) for x in intersect_position])


def decode_directions_intersect(input):
    rules = {('N', 'R'):['E', [1, 0]],
             ('N', 'L'):['W', [-1, 0]],
             ('S', 'R'):['W', [-1, 0]],
             ('S', 'L'):['E', [1, 0]],
             ('E', 'R'):['S', [0, -1]],
             ('E', 'L'):['N', [0, 1]],
             ('W', 'R'):['N', [0, 1]],
             ('W', 'L'):['S', [0, -1]]}
    starting_point = ['N', (0, 0)]
    current_state = starting_point
    already_seen = set([(0,0)])
    intersect_position = None
    for turn_to, move in input:
        facing, current_position = current_state
        [new_facing, move_rule] = rules[(facing, turn_to)]
        for m in move * [move_rule]:
            [x, y] = current_position
            [new_x, new_y] = m
            current_position = (x + new_x, y + new_y)
            if current_position in already_seen:
                intersect_position = current_position
                break
            else:
                already_seen.add(current_position)
        
        if intersect_position:
            break
        current_state = [new_facing, current_position]
    
    return sum([abs(x) for x in intersect_position])

def decode_directions(input):
    rules = {('N', 'R'):['E', [1, 0]],
             ('N', 'L'):['W', [-1, 0]],
             ('S', 'R'):['W', [-1, 0]],
             ('S', 'L'):['E', [1, 0]],
             ('E', 'R'):['S', [0, -1]],
             ('E', 'L'):['N', [0, 1]],
             ('W', 'R'):['N', [0, 1]],
             ('W', 'L'):['S', [0, -1]]}
    starting_point = ['N', [0, 0]]
    current_state = starting_point
    for turn_to, move in input:
        facing, current_position = current_state
        [new_facing, move_rule] = rules[(facing, turn_to)]
        new_position = [current_co_ord + (move * move_co_ord) for move_co_ord, current_co_ord in zip(move_rule, current_position)]
        current_state = [new_facing, new_position]
    return sum([abs(x) for x in current_state[1]])

def test_directions():
    assert 5 == decode_directions(string_to_list('R2, L3'))

    assert 2 == decode_directions(string_to_list('R2, R2, R2'))

    assert 12 == decode_directions(string_to_list('R5, L5, R5, R3'))

    assert 231 == decode_directions(read_directions_from_file('../directions.txt'))

def test_directions_intersect():
    assert 4 == decode_directions_intersect(string_to_list('R8, R4, R4, R8'))

    assert 147 == decode_directions_intersect(read_directions_from_file('../directions.txt'))

def test_directions_intersect_functional():
    assert 4 == decode_directions_intersect_functional(string_to_list('R8, R4, R4, R8'))

    assert 147 == decode_directions_intersect_functional(read_directions_from_file('../directions.txt'))
