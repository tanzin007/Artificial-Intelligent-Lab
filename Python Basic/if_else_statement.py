# The if statement alone tells us that if a condition is true it will execute a block of statements and 
# if the condition is false it won’t. 
# But what if we want to do something else if the condition is false. 
# Here comes the else statement. 
# We can use the else statement with if statement to execute a block of code when the condition is false. 

# python program to illustrate If else statement
#!/usr/bin/python

i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")