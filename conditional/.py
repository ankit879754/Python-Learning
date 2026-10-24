# Conditional Statement :-

# 1. if statement 
# 2. if - else 
# 3. if - elif
# 4. Nested if 

# 1. if statement :-  
# => whenever u have to apply condition for only one sceneraio , in that case u can use if statement. 

# a = int(input("hii, enter the value of a: "))

# if ( a == 10 ):
#                     print("the value of a : 10")

# --------------------------------------------------- 

# a = int(input("hii, enter the value of a: "))

# if ( a == 10 ):
#                     print("the value of a : 10")

# b = int(input("hii, enter the value of b: "))

# if ( b == 20 ):
#                     print("the value of b : 20")

# c = int(input("hii, enter the value of c: "))

# if ( c == 30 ):
#                     print("the value of c : 30")



# # 2. if - else :-
#  => whenever u have to apply condition for two sceneraio , in that case u can use if - else statement. 

# a = 10 
# b = 5

# if (a > b):
#                     print("a is greater")
# else:
#                     print("b is greater")

#  3. if - elif :-
#  => whenever u have to apply condition for more than two sceneraio , in that case u can use if - elif statement. 

a = int(input("Hii Vivek, Please enter the value of a : "))

if (a > 0 ):
                    print("a is Positive number")
elif (a < 0 ):
                    print("a is Negative number")
else:
                    print("a  is equal to 0")

# -----------------------------------------------------------------------------------------------------
# 4. Nested if :- 


# Ankit birtday :-


# if a box inside another box => this box is called NESTED BOX

# -------------------------------------------------------------- 

# age = 25
# salary = 30000

# if age >= 18:
#     print("Age criteria satisfied")

# else:
#     print("Loan Rejected: Age must be 18 or above")


# ----------------------------------------------------------- 

# age = 25
# salary = 30000

# if age >= 18:
#     print("Age criteria satisfied")

#     if salary >= 25000:
#         print("Loan Approved")
#     else:
#         print("Loan Rejected: Salary is too low")

# else:
#     print("Loan Rejected: Age must be 18 or above")


# -----------------------------------------------------------------


# age = int(input("Hii ANkit! please enter your age: "))

# if age >= 18:
#     print("Age criteria satisfied")

#     salary = int(input("Hii Ankit! please enter your salary:  "))

#     if salary >= 25000:
#         print("Loan Approved")
#     else:
#         print("Loan Rejected: Salary is too low")

# else:
#     print("Loan Rejected: Age must be 18 or above")

# ------------------------------------------------------------------- 


# age = 20
# citizen = "INDIAN"

# if age >= 18:
#     print("Age criteria satisfied")

#     if citizen == "INDIAN":
#         print("You are eligible to vote in INDIA")
#     else:
#         print("You must be INDIAN  to vote ")

# else:
#     print("You are not eligible to vote because your age is below 18")


# ------------------------------------------------------------------------ 



# age = int(input("hii, please enter your age : "))


# if age >= 18:
#     print("Age criteria satisfied")
     
#     citizen = input('hii, please type your citizenship: ')
#     if citizen == "INDIAN":
#         print("You are eligible to vote in INDIA")
#     else:
#         print("You must be INDIAN  to vote ")

# else:
#     print("You are not eligible to vote because your age is below 18")