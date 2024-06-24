def count_upper(mystring):
    i = 0
    for char in mystring:
        if char.isupper() is True:
            i += 1
    return i


print(count_upper('Welcome to WGU'))

print(count_upper('Hello, Mary'))
