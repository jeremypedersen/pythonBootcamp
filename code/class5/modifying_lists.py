# You can add lists together to make new lists
listA = ['Steve', 'Frank']
listB = ['Jim', 'Bill']

print(listA)
print(listB)

# You can add lists with "+"
names = listA + listB

print(names)

# You can find items in list using an index, like [0] or [1]
print(names[0])
print(names[2])

# You can also make a "slice", where you have an index that
# selects more than one thing from the list
print(names[0:2])

# There are also "special" index values, for instance [-1] always
# picks the LAST thing in the list, no matter how long it is
print(names[-1])

# Or [:] which means "pick everything in the list"
print(names[:])

# You can use [:] together with a number too! Like this
print(names[2:])