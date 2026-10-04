# Two Parameter List Slicing

# Two Parameter slicing ( starting point , ending point )
# ➢ By default the starting point will always be 0.
# ➢ By default the ending point will be always EXCLUDED.
# ➢ By default the ending point will be the last Index
# ____________________________
# Example 1:-
#  0 1 2 3 4 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6 ]
# print(my_list) print(my_list[ 0 ]) #→ Output = 11
print(my_list[ 0 : 3])
# Explanation:
# ➢ Starting Point = 0
# ➢ Ending point = 3 ( Excluded)
# ➢ So Final range 0 to 2
# Final Output = [11, 22, "Gulam"]
___________________________
# Example 2:-
#  0 1 2 3 4 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6 ]
print(my_list)
print(my_list[ 1 : 4])
# Explanation:
# ➢ Starting Point = 1
# ➢ Ending point = 4 ( Excluded)
# ➢ So Final range 1 to 3
# Final Output = [22, "Gulam", True ]
# ___________________________
# Example 3:-
#             0 1 2 3 4 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6 ]
print(my_list)
print(my_list[ 0 ]) #→ Output = 11
print(my_list[ : 3])
# Explanation:
# ➢ By default starting Point = 0
# ➢ Ending point = 3 ( Excluded)
# ➢ So Final range 0 to 2
# Final Output = [11, 22, "Gulam"]
# ___________________________
# Example 4: 0 1 2 3 4 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6 ]
print(my_list)
print(my_list[ 1 : ])
# Explanation:
# ➢ Starting Point = 1
# ➢ By default Ending point = Last index
# ➢ So Final range 1 to Last Index
# Final Output = [22, "Gulam", True, 55.6 ]
# ___________________________
# Example 5:-
#  0 1 2 3 4 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6 ]
print(my_list)
print(my_list[ : ])
# Explanation:
# ➢ By default Starting Point = 0
# ➢ By default Ending point = Last index
# ➢ So Final range 0 to Last Index
# Final Output = [11, 22, "Gulam", True, 55.6 ]

# ------------------------------------------------------------------------------------
# Three Parameter List Slicing
# Syntax
# List[start : end : gap]
# ➢ First parameter → Starting point
# ➢ Second parameter → Ending point
# ➢ Third parameter → GAP (N - 1)
# Note:
# ➢ By default Gap = 1 ___________________________
# Example List Slicing For Three perameter:-
# Example 1:-
#  0 1 2 3 4 5 6 7 8 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6, 66, 77, 88, 99]
print(my_list[0 : 4 ])# → Output = [ 11 , 22, "Gulam" , True]
print(my_list[0 : 4 : 1])
# Explanation:
# ➢ Starting point → 0
# ➢ Ending point → 4 (excluded)
# ➢ Gap = 1 → 1 - 1 = 0
# We have to skip 1 element at each iteration
# Final Output = [ 11 , 22, "Gulam" , True]
# ___________________________
# Example 2:-
#  0 1 2 3 4 5 6 7 8 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6, 66, 77, 88, 99]
print(my_list[0 : 4 : 2])
# Explanation:
# ➢ Starting point → 0
# ➢ Ending point → 4 (excluded)
# ➢ Gap = 2 → 2 - 1 = 1
# We have to skip 1 element at each iteration
# Final Output = [11, "Gulam",]
# ___________________________
# Example 3:-
#  0 1 2 3 4 5 6 7 8 → Indexing
my_list = [ 11 , 22, "Gulam" , True , 55.6, 66, 77, 88, 99] 
print(my_list[0 : 8 : 3])

# Explanation:
# ➢ Starting point → 0
# ➢ Ending point → 4 (excluded)
# ➢ Gap = 3→ 3 - 1 = 2
# We have to skip 2 element at each iteration
# Final Output = [ 11, True, 77]
___________________________
# What is Indentation
# ➢ Indentation in Python means the spaces or tabs at the beginning of a
# line of code.
# Example :-
print("Gulam")
print("Vivek")
___________________________
# input() Function
# ➢ It is used to take data from the user side.
# ➢ By default it gives string value.
# ➢ That’s why we have to specify the datatype.
# Example :-
a = int(input("Hii Vivek please Enter your value of a :"))
b = int(input("Hii Vivek please Enter your value of b :"))
print( a + b )
___________________________