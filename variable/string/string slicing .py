# There are 2 types of Slicing
# ➢ Two Parameter slicing ( starting point , ending point )
# ➢ Three parameter slicing ( Starting point , ending point , gap
# ______________________________________
# Slicing Rules :-
# Two Parameter String Slicing Two Parameter slicing ( starting point , ending point )
# ➢ By default the starting point will always be 0.
# ➢ By default the ending point will be always EXCLUDED.
# ➢ By default the ending point will be the last Index
# ______________________________________
# Example 1:-
# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10 →Indexing
my_string = "Programming"
print(my_string) # Programming
print(my_string[3:8])
# Explanation:-
# ➢ Starting Point = 3
# ➢ By default Ending point = 8 (EXCLUDED)
# ➢ So Final range 3 to 7
# Final Output = gramm
______________________________________
# Example 2 :-
print(my_string[2: ])
# Explanation:-
# ➢ Starting Point = 2
# ➢ By default Ending point = Last index
# ➢ So Final range 2 to Last Index
# Final Output = ogramming
______________________________________
# Three Parameter String Slicing
# Syntax
# String[start : end : gap]
# ➢ First parameter → Starting point
# ➢ Second parameter → Ending point ➢ Third parameter → GAP (N - 1)
# Note:
# ➢ By default Gap = 1
___________________________
# Example 1:-
# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g
my_string = "Programming"
print(my_string)
print(my_string[3:8]) #gramm
print(my_string[3:8:1])
# Explanation:-
# ➢ Starting point → 3
# ➢ Ending point → 8 (excluded)
# ➢ Gap = 1 → 1 - 1 = 0
# ➢ Final Gap = 0
# We have to skip 0 element at each iteration
# Final Output = gramm
___________________________
# Example 2:-
# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10 → Indexing
my_string = "Programming"
print(my_string)
print(my_string[3:8:2])
# Explanation:
# ➢ Starting point → 3
# ➢ Ending point → 8(excluded)
# ➢ Gap = 2 → 2 - 1 = 1
# ➢ Final Gap = 1
# We have to skip 1 element at each iteration
# Final Output = gam
___________________________