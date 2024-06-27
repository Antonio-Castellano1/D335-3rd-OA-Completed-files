# # Task 1 Complete the function that takes an integer as input and returns the factorial of that integer
# from math import factorial
#
#
# def calculate(x):
#     total = factorial(x)
#     return total
#
#
# print(calculate(3))  # expected outcome: 6
# print(calculate(9))  # expected outcome: 362880
#
# # Task 2 Complete the function that takes a list as input and returns a randomized item from that list
#
# import random as r
#
#
# def selection(x):
#     return r.choice(x)
#
#
# print(selection(['apple', 'banana', 'orange', 'grape']))
# print(selection([7, 5, 3, 9, 12, 4, 8, 10]))
#
# Task 3 Complete the function that takes as input an integer for a number of days and prints the total number of
# seconds in that number of days
#
# import datetime
#
#
# def current_date(x):
#     # seconds = datetime(days=x) # this seems alot harder and I don't get it do we use .date? .timedelta? time?
#     seconds = float(x * 86400)
#
#     print(seconds)
#
#
# current_date(4)
# current_date(7)

# # Task 4 Complete the function to return the current date
#
# import datetime as dt
#
#
# def currentDate():
#     return f'The current date is {dt.date.today()}'
#
#
# print(currentDate())  # Expected outcome will vary, but should follow this format: The current date is 9-11-2018.
#
# # Task 5 Complete the function that takes an integer as input, multiplies by e, and returns result rounded up
#
# from math import e, ceil
#
#
# def mathCalculation(x):
#     num = ceil(x * e)
#     return num
#
#
# # expected outcome: 9
# print(mathCalculation(3))
#
# # expected outcome: 25
# print(mathCalculation(9))

# # Task 6 Complete the function to return the number of leap years in the list
#
# import calendar
#
#
# # Complete the function to return the number of leap years in the list
# def countLeapYears(year_list):
#     return len([year for year in year_list if calendar.isleap(year)])  # I could not find this in the modules?
#     # count_year = 0
#     # for year in year_list:
#     #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     #         count_year += 1
#     #     else:
#     #         count_year += 0
#     # return count_year
#
#
# # expected output: 2
# print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))
#
# # expected output: 4
# print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))
#
# # Task 7 Complete the function to print the full name of the month using the calendar library
#
# import calendar
#
#
# # Complete the function to print the full name of the month using the calendar library
# def printMonthName(monthNum):
#     month = calendar.month_name[monthNum] # I also could find this anywhere in the modules
#     print(month)
#
#
# # expected output: March
# printMonthName(3)
#
# # expected output: November
# printMonthName(11)
#
# Task 8 Complete the function to print the full name of the day of the week
#
# import datetime
# import calendar
#
#
# # Complete the function to print the full name of the day of the week
# def printWeekdayName(year, month, day):
#     day_name1 = calendar.weekday(year, month, day)  # where do i use datetime ??
#     day_name2 = calendar.day_name[day_name1]
#
#     print(day_name2)
#
#
# # expected output: Friday
# printWeekdayName(2001, 8, 31)
#
# # expected output: Monday
# printWeekdayName(2018, 10, 1)

# # Task 9 Complete the following function to return a random number between 5 and 8 exclusive
#
# import random
# #
# #
# # # Complete the following function to return a random number
# # # between 5 and 8 exclusive
# def getRandom():
#     return random.randint(5, 7)
#
#
# # expected output: You should only get 5s, 6s, and 7s
# for i in range(10):
#     print(getRandom())

# Task 10 Complete the function to add 90 days to the given date and return the new date
#
# import datetime
#
#
# # Complete the function to add 90 days to the given date and return the new date
# def add90Days(someDate):
#     return someDate + datetime.timedelta(days=90) # i cant find this in modules either
#
#
# # expected output: 2018-12-30
# print(add90Days(datetime.date(2018, 10, 1)))
#
# # expected output: 2015-05-12
# print(add90Days(datetime.date(2015, 2, 11)))
