"""2.Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error"""

password=input("enter your password:")
confirmed_pass=input("enter your NEW PASSWORD:")
if password==confirmed_pass:
    print("Password set successfull")
else: 
    print("Error occured during validation")

