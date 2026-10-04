Binary Number
0000 => 0
0001 => 1
0010 => 2
0011 => 3
0100 => 4
0101 => 5
0110 => 6
0111 => 7
1000 => 8
1001 => 9
1010 => 10 => A
1011 => 11 => B
1100 => 12 => C
1101 => 13 => D
1110 => 14 => E
1111 => 15 => F
➢ TRUE → 1
➢ False → 0
_____________________________
Rules:-
➢ Bitwise &
○ If both cases are 1, it gives 1 otherwise it gives 0.
➢ Bitwise |
○ If both cases are 0, it gives 0 otherwise it gives 1. _____________________________
Example Calculation:-
3 5 6
+ 2 4 3
-----------
5 9 9
_____________________________
Example 1:-
a = 10 , binary number of 10 → 1010
b = 3 , binary number of 3 → 0011
print(a & b)
Binary Calculation:
1 0 1 0 => binary of 10
& 0 0 1 1 => binary of 3
---------------
0 0 1 0 => binary of 2
_____________________________
Example 2:-
a = 14 , binary number of 14 → 1110
b = 11 , binary number of 11 → 1011
print(a & b)
1 1 1 0
& 1 0 1 1
---------------
1 0 1 0 => binary number of 10
_____________________________
Example 3:-
a = 14 ,binary number of 14 → 1110
b = 11 ,binary number of 11 → 1011 print(a | b)
1 1 1 0
| 1 0 1 1
----------------
1 1 1 1 => binary number of 15