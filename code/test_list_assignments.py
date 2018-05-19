names = ["Linus", "Trovalds"]
assert(__ == names)

first_name, last_name = names
assert(__ == first_name)
assert(__ == last_name)

first_name, last_name = [["Guido", "van"], "Rossum"]
assert(__ == first_name)
assert(__ == last_name)
    
first_name = "Linus"
last_name = "Trovalds"
first_name, last_name = last_name, first_name
assert(__ == first_name)
assert(__ == last_name)
