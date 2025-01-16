"""2.Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program."""
def cal(text):
    
    upper=0
    lower=0
    for a in text:
        if a.isupper():
            upper+=1
        else:
            lower+=1
    return upper,lower
def Trax():
    rax=input("enter your text: ")
    up,low=cal(rax)
    return up,low
OUT,PUT=Trax()
print(f'Number of uppercase letters "{OUT}" and lowercase letters "{PUT}"')