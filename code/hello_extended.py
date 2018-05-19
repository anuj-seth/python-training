#!/usr/bin/env python

print("Hello world")

def hanoi():
    yield 0
    last = 0
    while True:
        current = (2 * last) + 1
        yield current
        last = current

moves = [x for x in zip(hanoi(), xrange(1000 + 1))][-1][0]

print moves

def rec_hanoi(n):
    if n == 0:
        return 0
    else:
        return (2 * rec_hanoi(n-1)) + 1

#print rec_hanoi(1000)


def my_gen():
    yield 'a'
    yield 'b'

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
    return

def square_me(seq):
    for x in seq:
        yield x * x

result = square_me(range(2, 5))
assert(__ == list(result))


def sum_it(seq):
    value = 0
    for num in seq:
        # The local state of 'value' will be retained between iterations
        value += num
        yield value

result = sum_it(range(2, 5))
assert(__ == list(result))
