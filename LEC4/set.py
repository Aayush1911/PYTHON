# Set is collection of the unordered(no index) items
# Each element in set must be unique and immutable(not changeable)
# set is mutable but its element are immutable

# list and dictionaries are not stored in set because they are mutable but set is immutable

set={1,2,3,4,5,6,5,2,'hello','world','hello'} #duplicate values are ignored and it stored only once
# print(set) #{1, 2, 3, 4, 5, 6, 'hello', 'world'}
# print(type(set)) #<class 'set'>

# to create empty set
# collection=set()
# print(type(collection))

# methods
# set.add(8)
# set.add([45,17]) #list can not be added to set
# print(set)

# set.remove(6)
# print(set)

# set.clear()
# print(set)

# print(len(set))

# set.pop()
# print(set)

set1={1,2,3,4,5}
set2={1,2,4,10,11,12}
# union and intersection makes new set not updates it
# print(set1.union(set2))
# print(set1.intersection(set2))

