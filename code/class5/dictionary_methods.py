# Let's start with a simple dictionary
d = {
    'apples': 5,
    'bananas': 6,
    'grapefruit': "I don't like grapefruit!"
}

print(d)

# We can add things...
d['oranges'] = 100

print(d)

# We can get a list of the keys
print( d.keys() )

# Or the values
print( d.values() )

# Or everything (key/value pairs)
print( d.items() )

# We can also check whether or not something is
# inside the dictionary, with get()
print( d.get('oranges', 0) )
print( d.get('elephants', 0) )

# We can remove something (by key) and return
# its value
print( d.pop('grapefruit') )
print(d)

# We can also remove something (by key-value pair) and then
# return the key-vlue pair
print( d.pop('bananas', 6) )
print(d)
