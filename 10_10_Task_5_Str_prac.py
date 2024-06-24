# Complete the function to combine the words into a sentence and return a string
def combine_words(words):
    new_string = ' '.join(words)
    return new_string


# expected output: WGU College of IT
print(combine_words(['WGU', 'College', 'of', 'IT']))
print(combine_words(['Night', 'Owls', 'Rock']))
