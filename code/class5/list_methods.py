myList = ['Glenn', 'Sarah', 'Elizabeth']

# Add one thing to the list
myList.append('Frank')

print(myList)

# Add more than one thing to the list
myList.extend(['Carl', 'Sandy', 'Ralph'])

print(myList)

# Reverse all the items in the list
myList.reverse()

print(myList)

# Sort the list (from biggest to smallest for numbers, from A-Z for words)
myList.sort()

print(myList)

# Remove the last item from the list, and return it (so we can save it into a variable)
print( myList.pop() )
print (myList)

# Remove a specific thing
myList.remove('Ralph')

print(myList)

# Insert something at a specific spot
myList.insert(1, 'Bob')

print(myList)

# Find how many times something is in the list
print( myList.count('Sandy') )
