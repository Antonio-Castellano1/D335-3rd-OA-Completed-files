def remove_wgu(mystring):
    if mystring[:3] == 'WGU':
        return mystring
    elif mystring[:3] != 'WGU':
        new_string = mystring.replace('WGU', '')
        return new_string


print(remove_wgu('WGU Rocks'))

print(remove_wgu('Hello, WGUJohn'))
