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
