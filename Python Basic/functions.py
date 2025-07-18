# A function in python is declared by the keyword 'def' before the name of the function. 

# The return type of the function need not be specified explicitly in python. 

# The function can be invoked by writing the function name followed by the parameter list in the brackets.


# Function for checking the divisibility

# Notice the indentation after function declaration

# and if and else statements

def checkDivisibility(a, b):
    if a % b == 0 :
        print ("a is divisible by b")
    else:
        print ("a is not divisible by b")


#Driver program to test the above function
checkDivisibility(4, 2)