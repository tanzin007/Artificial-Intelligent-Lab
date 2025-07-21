# In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement. 
# With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type.  
# Various forms of explicit type conversion are explained below:

# int(a, base): This function converts any data type to integer.
# float(): This function is used to convert any data type to a floating-point number.


# Python code to demonstrate Type conversion
# using int(), float()

# initializing string
s = "10010"

# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)

# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)