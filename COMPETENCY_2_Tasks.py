# Task 1
# create a function with receives two integers as input, adds them and returns the sum
# def two_num_sum(num1, num2):
#     total = num1 + num2
#     return total
#
#
# num_1 = int(input())
# num_2 = int(input())
#
# print(two_num_sum(num_1, num_2))

# run your function and print the result with integers 7 and 9
# expected outcome: 16
# print(two_num_sum(7, 9))

# run your function and print the result with integers 20 and 49
# expected outcome: 69
# print(two_num_sum(20, 49))

# Task 2 Run the same function above with integers 2 and 8, and save the output to a new variable called myNewSum.
# Print myNewSum.

# expected outcome: 10
# myNewSum = two_num_sum(2, 8)
# print(myNewSum)


# Task 3
# You are provided a student's score on the recent exam.
# Create a function that will print a reply based on the score.
# Students who score 90 points or more receive an A and pass the course
# Students receiving 80 points or more receive a B and pass the course.
# Students receiving 79 points or fewer do not pass and need to retake the exam.
# Students receiving a score of 0 have not attempted the exam and need instructions to schedule.
# def grade_report(num):
#     if num == 0:
#         return 'You have not attempted the exam. Here are instructions to schedule.'
#
#     if num >= 90:
#         return 'You received an A and have passed the course.'
#
#     if 80 <= num < 90:
#         return 'You have not passed the course. Please retake the exam.'
#
#     if num <= 79:
#         return 'You have not passed the course. Please retake the exam.'
#
#
# print(grade_report(90))  # expected outcome: You received an A and have passed the course.
#
# print(grade_report(70))  # expected outcome: You have not passed the course. Please retake the exam.

# Task 4
# use the range method to print out numbers 6-12
# for nums in range(6, 13):
#     print(nums)


# Task 5
# create a list containing the names Dana, Cemal, Jessica, Mike, and Dana

# name_list = ['Dana', 'Cemal', 'Jessica', 'Mike', 'Dana']
# print(name_list)

# Task 6
# Print the length of the list.
# print(len(name_list))

# expected outcome: 5


# Task 7
# Check to see if David is in the list. If not in the list, add her and print the list.
# if 'David' not in name_list:
#     name_list.append('David')
#     print(name_list)

# expected outcome: ['Dana', 'Cemal', 'Jessica', 'Mike', 'Dana', 'David']


# Task 8
# Print a single string containing all the names separated by commas
# new_list = ', '.join(name_list)
# print(new_list)
# expected outcome: Dana, Cemal, Jessica, Mike, Dana, David


# Task 9
# Print only the names Dana and Mike from myNames. Note the date type below.
# print(name_list[3:5])

# expected outcome: ["Mike","Dana"]


# Task 10
# uni_list = set(name_list)

# print(uni_list)
# ensure that each name is only listed once and print the list of unique values
# expected outcome: ['Dana', 'Cemal', 'Jessica', 'Mike', 'David'] *note: order of items in list may vary


# Task 11
# create an individual message for each unique name and welcome them to WGU
# for name in uni_list:
#     print(f'Welcome to WGU, {name}')
# expected outcome: Welcome to WGU, Dana
#                   Welcome to WGU, Jessica
#                   Welcome to WGU, Mike
#                   Welcome to WGU, David
#                   Welcome to WGU, Cemal


# Task 12 Given the following dictionary of employees and salaries, create a personalized salary message letting each
# employee know they have been given a 2% raise and the new total of their salary.

# expected outcome:

# John, your current salary is 54000.00. You received a 2% raise. This makes your new salary 55080.0
# Judy, your current salary is 71000.00. You received a 2% raise. This makes your new salary 72420.0
# Albert, your current salary is 38000.00. You received a 2% raise. # This makes your new salary 38760.0
# Alfonzo, your current salary is 42000.00. You received a 2% raise. This makes your new salary 42840.0


# employeeDatabase = {
#     'John': 54000.00,
#     'Judy': 71000.00,
#     'Albert': 38000.00,
#     'Alfonzo': 42000.00
# }
# for name in employeeDatabase:
#     print(f'{name}, your current salary is {employeeDatabase[name]}. You received a 2% raise. This makes your new '
#           f'salary {(employeeDatabase[name] * .02) + employeeDatabase[name]}')

# Task 13
# starting with year 2000, create a list containing 5 leap years
# when the list is complete, print the full list with a message
# year = 2000
# leap_year_list = []
# not_leap_year_list = []
# while len(leap_year_list) < 5:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         leap_year_list.append(year)
#         year += 1
#     else:
#         not_leap_year_list.append(year)
#         year += 1
# print(leap_year_list)

# expected outcome: These are the leap years: [2000, 2004, 2008, 2012, 2016]


# Task 14
# A nurse is monitoring a patient's rising temperature. The temp is rising in increments of .5 degrees continually.
# The nurse needs to be shown a message when the temp reaches 104 and the monitoring should end at that time.
# temp = 98.6
# while temp <= 104.0:
#     temp += .5
# if temp >= 104.0:
#     print('The temp has reached 104.0')


# expected outcome: The temp has reached 104.0


# Task 15a create a tuple to store the WGU phone number 877-435-7948. Store the phone number as three groups of
# numbers without the hyphens.
# wgu_phone_number = (877, 435, 7948)


# Task 15b
# use the tuple to print the last four digits of the phone number
# print(wgu_phone_number[2])
# expected outcome: 7948


# Task 15c
# use the tuple to print the entire phone number with the message to Call WGU now
# print(f'Call WGU now at {wgu_phone_number[0]}-{wgu_phone_number[1]}-{wgu_phone_number[2]}')
# expected outcome: Call WGU now at 877-435-7948


# Task 16 Finish the function to take as input a list of fruits and return a string value containing the first two
# fruits from the list

# def fruitFunction(fruits):
#     return f'{fruits[0]} {fruits[1]}'
#
#
# print(fruitFunction(['banana', 'apple', 'orange', 'grapes', 'pineapple']))  # expected outcome: banana apple
# print(fruitFunction(['mango', 'avocado', 'pear']))  # expected outcome: mango avocado

# Task 17 Finish the function to take as input a list of fruits and return a string value letting us know if the
# avocado is in the list or not. If so, state that the avocado is in the list. If not, state avocado not found.

# def fruitFunction2(fruits):
#     if 'avocado' in fruits:
#         return 'avocado is in the list'
#     else:
#         return 'avocado not found'
#
#
# print(fruitFunction2(['pear', 'apple', 'lemon', 'grapes', 'pineapple']))  # expected outcome: avocado not found
# print(fruitFunction2(['lime', 'avocado', 'pear']))  # expected outcome: avocado is in the list


# Task 18 Finish the function that takes as input a list of foods and returns a count of the number of times pizza is
# included in the list of favorite foods.

# def favFoods(x):
#     check_list = []
#     for food in x:
#         good_spell_food = food.lower()
#         check_list.append(good_spell_food)
#     num_pizza = check_list.count('pizza')
#
#     return num_pizza
#
#
# print(favFoods(['apple', 'banana', 'pizza', 'Pizza', 'ice cream', 'cupcakes']))  # expected output: 2
# print(favFoods(['almonds', 'spaghetti', 'pizza', 'kombucha', 'Pizza', 'pizza']))  # expected output: 3


# Task 19 Completed the function that takes as input a string value of names and returns each name as an individual
# item in a list.

# def makeList(names):
#     new_list = names.split()
#     print(new_list)
#
#
# print(makeList( 'Jessica John Paul Grace Ginger Billy Arlene'))  # expected output: ['Jessica', 'John', 'Paul',
# 'Grace', 'Ginger', 'Billy', 'Arlene'] print(makeList( 'David Cemal Dana Rodger Jerry Jessica Mike'))  # expected
# output: ['David', 'Cemal', 'Dana', 'Rodger', 'Jerry', 'Jessica', 'Mike']


# Task 20
# Complete the function that takes one argument as a list of expenses and returns the total cost of all purchases.

# def costCount(purchases):
#     total = 0
#     for item in purchases:
#         total += item
#     return total
#
#
# print(costCount([39.90, 40.21, 8.73, 9.57]))  # expected output: 98.41
# print(costCount([139.90, 10.11, 1.53, 3.57]))  # expected output: 155.10999999999999
