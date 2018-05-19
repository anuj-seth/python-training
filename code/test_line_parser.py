import string

def line_parser(keys, in_string, delim):
    pass

def test_line_parser():
    keys = ['ip-address', 'timestamp', 'duration']
    in_string = '10.1.17.99;2017-11-11 12:32:42;5'
    delim = ';'
    out_map = {'ip-address':'10.1.17.99', 'timestamp':'2017-11-11 12:32:42', 
               'duration':'5'}
    assert(out_map == line_parser(keys, in_string, delim))

    keys = 'abcd'
    in_string = 'a b c d'
    delim = ' '
    out_map = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'}
    assert(out_map == line_parser(keys, in_string, delim))
