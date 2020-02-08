# You create a new dictionary like this
d = {}

# You can add new items like this
d['bananas'] = 5
d['apples'] = 2
d['oranges'] = 'we have no oranges'

print(d)

# You can use regular functions like "len", "min", and "max"
# like you did for lists, but remember these functions will 
# look at the KEYS (item names) in the dictionary, not their
# VALUES. This is important!
print( max(d) )
print( min(d) )
print( len(d) )
