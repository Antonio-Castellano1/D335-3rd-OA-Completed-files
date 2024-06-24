# Complete the function to return True if the word WGU exists in the given string
# otherwise return False
def containsWGU(mystring):
    boolean_value = bool('WGU' in mystring)
    return boolean_value


print(containsWGU('WGU College of IT'))
print(containsWGU('Night Owls Rock'))
