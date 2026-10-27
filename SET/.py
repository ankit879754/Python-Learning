Set Methods
add()
remove() → if element is not found, it gives error
discard() → if element is not found, it does not give any error
pop() → it removes any random element

✔ Examples:
# my_set = {11,22,33}
# print("before", my_set)

# my_set.add(100)
# print("after", my_set)

# my_set = {11,22,33}
# print("before", my_set)

# my_set.remove(11)
# print("after", my_set)

# my_set = {11,22,33}
# print("before", my_set)

# my_set.discard(111)
# print("after", my_set)

# my_set = {11,22,33,123}
# print("before", my_set)

# my_set.pop()
# print("after", my_set)

# my_set = {11,22,33,123}
# print("before", my_set)

# my_set.clear()
# print("after", my_set)

________________________________________________
Set Operations (Mathematics)
A = {11,22,33}
B = {11,22,333}

print("union", A.union(B))
print("intersection", A.intersection(B))

Union → similar elements and rest of elements
Intersection → only similar elements