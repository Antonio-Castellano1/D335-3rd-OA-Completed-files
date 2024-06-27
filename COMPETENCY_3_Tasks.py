# Task 1
# use the math module to determine the factorial of the number 7 and print the result
# import math
# print(math.factorial(7))
# expected outcome: 5040
import math
# Task 2
# use the math module to determine the square root of the number 27 and print the result

# expected outcome: 5.196152422706632
# import math
# print(math.sqrt(27))

# Task 3
# use the math module to determine the largest integer less than or equal to 15.87 and print the result

# expected outcome: 15
# import math
# print(math.floor(15.87))

# Task 4
# use the math module to determine the smallest integer greater than or equal to 15.87 and print the result

# expected outcome: 16
# import math
# print(math.ceil(15.87))

# Task 5
# use the math module to determine e to the power of 4

# expected outcome: 54.598150033144236
# from math import e
# print(math.pow(e, 4))

# Task 6
# complete the function that determines the nearest whole number for x and prints the result
# def nearest(x):
#     num = round(x)
#     print(num)
#
#
# nearest(15.87)  # expected result: 16
# nearest(7.21)  # expected result: 7
#
#
# # Task 7
# # complete the function that determines the square root of x, rounded to the nearest whole number.
#
# import math
#
#
# def square(x):
#     num = round(math.sqrt(x))
#     print(num)
#
#
# square(38)  # expected result: 6
# square(58)  # expected result: 8

# ---- Random Module --- ##

# Task 1
# use the random module to print a random integer between 2 and 20, exclusive
# import random
# print(random.randint(3, 19))

# Task 2
# use the random module to print a random number from the range 1 to 100, inclusive
# import random
# print(random.randint(1, 100))

# Task 3
# use the random module to return a random floating point number
# import random
# print(float((random.random())))

# Task 4
# Create a list of 6 words. Then use the random module to return a random element from that list.
# import random
# listy = ['momo', 'rajah', 'zuzu', 'tony', 'python', 'crying']
# print(random.choice(listy))

# ---- OS Module --- ##

# Task 1
# use the os module to create a hard link to C://myfile.txt at C://myPython/myfile.txt
# import os
#
# source = "C://myfile.txt"
# link_name = "C://myPython/myfile.txt"
#
# os.link(source, link_name)

# Task 2
# use the os module to delete the file C://myfile.txt
# import os
#
# os.remove('C://myfile.txt')


# Task 3
# use the os module to return the current working directory
# import os
#
# current_dirc = os.getcwd()


# Task 4
# use the os module to change the root directory to C://home/

# import os
#
# os.chdir('C://home/')

# ---- Datetime Module --- ##

# Task 1
# use the datetime module to print the current year
# import datetime
# print(datetime.datetime.now().year)

# Task 2
# use the datetime module to print the current month
# import datetime
# print(datetime.datetime.now().month)

# Task 3
# use the datetime module to print the current day
# import datetime
# print(datetime.datetime.now().day)

# Task 4
# use the datetime module to print the total number of seconds in 4 days
# expected outcome: 345600.0

# import datetime
#
# day_total = datetime.timedelta(days=4)  # this seems alot harder and I don't get it do we use .date? .timedelta? time?
# second_total = day_total.total_seconds()
#
# print(second_total)


# Task 5
# print today's date one year from now
# from datetime import datetime, timedelta
#
# today = datetime.today()
# one_year_later = today + timedelta(days=365)
#
# print(one_year_later)
#

# ---- Lookup  --- ###
# Task 1
# You need to use the datetime library to account for time zone adjustments, but aren't sure which method(s) to use.
# You are taking an exam and can't google it. What Python function will allow you to look up and locate the method?
# Write your code below:
# import datetime
#
# # print(help(datetime)) # used this to help
# print(help(datetime.timezone))



# Task 2 What built-in function would allow me to see ONLY a list of the methods (not the full documentation)
# associated with a type of object? Call this function on the str data type. Note that you will need to print() the
# call to this function.

# print(dir(str))
