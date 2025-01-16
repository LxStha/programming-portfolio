"""1.Functions are oen used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function."""
def fun():
    value_=int(input("enter your value: "))
    return value_
def chack():
    if fun()<=100:
        print("True")
    else:
        print("False")
chack()