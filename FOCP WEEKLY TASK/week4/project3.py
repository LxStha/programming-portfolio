"""3.Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name dierently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.
"""
def nam():
    return input("Hello user pls enter your name: ")
def cap():
    name=nam()
    latter=name[0].upper()
    return latter+name[1:].lower()
print(f"Helloi, {cap()}")