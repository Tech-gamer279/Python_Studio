# Conditional statements in Python
# This code snippet demonstrates how to use conditional statements in Python.

# Conditional statements allow you to execute different blocks of code based on certain conditions.
# This code snippet demonstrates how to use conditional statements in Python.

# Define a variable
age = 18
# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
# Check if the age is less than 13
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")


# Check if the age is exactly 18
if age == 18:
    print("You are exactly 18 years old.")
else:    print("You are not 18 years old.")

# Check if the age is not equal to 18
if age != 18:
    print("You are not 18 years old.")
else:
    print("You are 18 years old.")

# Check if the age is less than or equal to 18
if age <= 18:
    print("You are 18 years old or younger.")
else:
    print("You are older than 18 years old.")


# Check if the age is greater than or equal to 18
if age >= 18:
    print("You are 18 years old or older.")
else:
    print("You are younger than 18 years old.")

# Check if the age is between 13 and 19 (inclusive)
if 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")    
# Check if the age is not between 13 and 19 (inclusive)
if not (13 <= age <= 19):
    print("You are not a teenager.")
else:
    print("You are a teenager.")

# Check if the age is in a specific range
if age in range(13, 20):
    print("You are a teenager.")
else:
    print("You are not a teenager.")


"""
==========================================
Python Conditional Statements Tutorial
==========================================

Conditional statements allow you to execute different blocks of code based on certain conditions.
They are fundamental for decision-making in Python programs.

------------------------------------------
1. Basic if Statement
------------------------------------------
    if condition:
        # code to execute if condition is True

Example:
    age = 18
    if age >= 18:
        print("You are an adult.")

------------------------------------------
2. if-else Statement
------------------------------------------
    if condition:
        # code if True
    else:
        # code if False

Example:
    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

------------------------------------------
3. if-elif-else Statement
------------------------------------------
    if condition1:
        # code if condition1 is True
    elif condition2:
        # code if condition2 is True
    else:
        # code if none are True

Example:
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

------------------------------------------
4. Comparison and Logical Operators
------------------------------------------
- ==  (equal to)
- !=  (not equal to)
- <   (less than)
- >   (greater than)
- <=  (less than or equal to)
- >=  (greater than or equal to)
- and, or, not

Example:
    if 13 <= age <= 19:
        print("You are a teenager.")

------------------------------------------
5. Using range() and in
------------------------------------------
    if age in range(13, 20):
        print("You are a teenager.")

------------------------------------------
6. More Information
------------------------------------------
- Official Python docs: https://docs.python.org/3/tutorial/controlflow.html#if-statements

See below for code examples.
"""
# ...existing code...

# I don't know whether this shall change in the later future

# Looks Good code?

# Check out the ZEN OF PYTHON, cuz thats OP