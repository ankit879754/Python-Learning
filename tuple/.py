TUPLE:-
Tuple is a data structure , it is immutable ( it can be changed only entirely not specifically)
It is a collection of items , just like a list .
It can store any type of value just like a list.
it is enclosed with parentheses ().

my_tuple = ("Ankit",55, 6.6, True)

print(my_tuple)
______________________________________

How to apply a loop in Tuple :-

 my_tuple = ("Ankit",55, 6.6, True)

for i in my_tuple:
     print(i)
Tuple Methods:
count()
index()
                       0  1  2   3  4  5  6  7
my_tuple = (11,22,333,33,33,44,33,33)

print(my_tuple.count(33))  4
print(my_tuple.index(33))   3