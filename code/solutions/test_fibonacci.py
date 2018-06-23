def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def test_fib():
    assert 0 == fib(0)
    assert 1 == fib(1)
    assert 21  == fib(8)
