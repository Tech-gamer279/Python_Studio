"""
==========================================
Python Tips and Tricks
==========================================

Here are some useful tips and tricks to help you write better Python code:

------------------------------------------
1. Multiple Variable Assignment
------------------------------------------
    a, b, c = 1, 2, 3

------------------------------------------
2. Swapping Variables
------------------------------------------
    x, y = y, x

------------------------------------------
3. List Comprehensions
------------------------------------------
    squares = [x**2 for x in range(10)]

------------------------------------------
4. Enumerate for Index and Value
------------------------------------------
    for idx, value in enumerate(['a', 'b', 'c']):
        print(idx, value)

------------------------------------------
5. Use '_' for Unused Variables
------------------------------------------
    for _ in range(5):
        print("Hello")

------------------------------------------
6. Joining Strings
------------------------------------------
    words = ['Python', 'is', 'fun']
    sentence = ' '.join(words)

------------------------------------------
7. Dictionary Get with Default
------------------------------------------
    my_dict = {'a': 1}
    value = my_dict.get('b', 0)  # Returns 0 if 'b' not found

------------------------------------------
8. Context Managers for Files
------------------------------------------
    with open('file.txt') as f:
        data = f.read()

------------------------------------------
9. F-Strings for Formatting
------------------------------------------
    name = "Alice"
    print(f"Hello, {name}!")

------------------------------------------
10. Zen of Python
------------------------------------------
    import this [A good phillosphy To read]

For more tips, see the official Python documentation:
https://docs.python.org/3/tutorial/datastructures.html"""