# this is how we can handle multiple exceptions
import sys
try:
    f = open('integers.txt')
    s = int(f.readline().strip())
except IOError as e: 
    print("I/O error({0}): {1}".format(e.args[0], e.args[1]))
except ValueError as v:
    print("ValueError: {0}".format(v.args))
except:
    print("Unexpected error: {0}".format(sys.exc_info()[0]))
    raise
else:
    print("we will get here if no exception raised")
finally:
    print("do any cleanup here")
