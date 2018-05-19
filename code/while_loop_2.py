#!/usr/bin/env python
n = 100

the_sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        i = i + 1
        continue
    the_sum = the_sum + i
    i = i + 1

print("Sum of odd numbers from 1 until {0}: {1}".format(n, 
                                                        the_sum))
