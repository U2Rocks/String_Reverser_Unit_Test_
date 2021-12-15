# this function reverses a string

def reverse_string(text):
    if type(text) == int:
        raise(TypeError("You must enter a string!"))
    if type(text) == list:
        raise(TypeError("You must enter a string!"))
    string_to_reverse = [letter for letter in text]
    new_string = ""
    for letter in string_to_reverse:
        new_string = letter + new_string
    return new_string

