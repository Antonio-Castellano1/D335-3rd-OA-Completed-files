def printFirst(mystring, x):
    print(mystring[:x])

printFirst('WGU College of IT', 3)
# expected output: WGU College
printFirst('WGU College of IT', 11)

def printFirst(mystring, x):
    print(mystring[-x:])

printFirst('WGU College of IT', 2)
# expected output: WGU College
printFirst('WGU College of IT', 13)

def containsWGU(mystring):
    boolean_value = bool('WGU' in mystring)
    return boolean_value


print(containsWGU('WGU College of IT'))
print(containsWGU('Night Owls Rock'))
def print_words(mystring):
    string_list = mystring.split()
    print(string_list)


print_words('WGU College of IT')

print_words('Night Owls Rock')

def combine_words(words):
    new_string = ' '.join(words)
    return new_string


# expected output: WGU College of IT
print(combine_words(['WGU', 'College', 'of', 'IT']))
print(combine_words(['Night', 'Owls', 'Rock']))

def replace_wgu(mystring):
    new_string = mystring.replace('WGU', 'Western Governors University')
    return print(new_string)


replace_wgu('WGU Rocks')

replace_wgu('Hello, WGU')

def remove_wgu(mystring):
    if mystring[:3] == 'WGU':
        return mystring
    elif mystring[:3] != 'WGU':
        new_string = mystring.replace('WGU', '')
        return new_string


print(remove_wgu('WGU Rocks'))

print(remove_wgu('Hello, WGUJohn'))

def remove_spaces(string1, string2):
    trail_space_gone = string1.split()
    leading_space_gone = string2.split()

    new_str1 = ' '.join(trail_space_gone)
    new_str2 = ' '.join(leading_space_gone)

    whole_string = new_str1 + new_str2

    return whole_string


# expected output: WGU Rocks-You know it!
print(remove_spaces('WGU Rocks    ', '  -You know it!'))

# expected output: Welcome WGU-IT Students
print(remove_spaces('Welcome WGU ', ' -IT Students'))

def display_hourly_rate(rate):
    est_rate = f'{rate:.2f}'
    print(est_rate)


display_hourly_rate(34.789123)

display_hourly_rate(24.123456)

def count_upper(mystring):
    i = 0
    for char in mystring:
        if char.isupper() is True:
            i += 1
    return i


print(count_upper('Welcome to WGU'))

print(count_upper('Hello, Mary'))
