# Type of Function :- 

# 1. Function with parameters
#    a. Default arguments
#    b. Positional arguements
# 2. Function without Parameters

# ------------------------------------------------------------- 

# 1. Function without Parameters :- 
# => it has no parameters.

# Example :- 

# def print_all_std_name():
#                     print("Neha")
#                     print("ANkit")

# print_all_std_name()


# 2. Function with parameters :- 

# => it has parameters. 

# a. Positional arguments :- 

# Example:- 

# def sum_of_two_number(a,b):
#                     print("the sum of a and b : ", a + b)

# sum_of_two_number(20,28)
# sum_of_two_number(20,280)

# ---------------------------------------------------- 

b. Default Parameters :- 

# def sum_of_two_number(a, b = 50):
#                     print("the sum of a and b: ", a + b)

# sum_of_two_number(20)

# -------------------------------------------------- 

def sum_of_two_number(a, b = 50):
                    print("the sum of a and b: ", a + b)

sum_of_two_number(20,89)