# create a file file_reader.py
fobj = open('file_reader.py', 'r')

for line in fobj:
    # note the trailing comma
    # we could have also done line.rstrip()
    print(line),

fobj.close()
