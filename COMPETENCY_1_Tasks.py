a, b, c = 1, 2, 3

float(a)
float(b)
float(c)

str(a)
str(b)
str(c)

result = 783.56 / 123.2
print(int(result))

leap_result = 2019 % 4
print(leap_result)

myFirstString = 'I love working with Python so much!'

print(len(myFirstString))

string_value = 'i really love using python!'

new_string = string_value.title()

print(new_string)

string_value = 'i really love using python!'

yes_no = string_value.islower()

print(yes_no)

commercial = 'In the Little Ceasars pizza commercial the character says, "pizza, pizza"!'

num = commercial.count('pizza')

print(num)

username = 'Allen'
phone = '8885550011'

print(f'Hi, {username}. I will call you at {phone[:3]}-{phone[3:6]}-{phone[6:10]} for our appointment.')