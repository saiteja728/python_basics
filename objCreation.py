#how many ways we can create objects explained here below
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
# obj = MyClass(42)  # Creating an instance of MyClass

#using built-in functions:
num = int(42)  # Creating an integer object
my_list = list(range(3))  # Creating a list object
print(num)


#using literals:
num = 42  # Creating an integer object
pi = 3.14  # Creating a floating-point object
print(pi)

#using string:
my_string = "Hello, World!"  # Creating a string object

#using object copying:
original_list = [1, 2, 3]
new_list = original_list.copy()  # Creating a new list by copying the original
print(new_list)

#using list comprehensions and list generators
squared_numbers = [x**2 for x in range(1, 6)]  # Creating a list of squared numbers
print(squared_numbers)

#factory functions:
from datetime import datetime
now = datetime.now()  # Creating a datetime object representing the current date and time

#specialized constructiors:
# file = open("example.txt", "r")  # Creating a file object


