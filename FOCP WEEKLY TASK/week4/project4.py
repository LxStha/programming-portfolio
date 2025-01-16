"""4.When processing data it is oen useful to remove the last character from some
input (it is oen a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)"""
def name():
    return input("Enter your text:")
def remo():
    text=name()
    if len(text)<=1:
        print(text)
    else:
        text=text[:-1]
        print(text)
remo()