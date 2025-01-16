"""3.Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long."""

password=input("enter your password:")
confirmed_pass=input("enter your NEW PASSWORD:")

if 8<= len(password) <=12:
    if password==confirmed_pass:
        print("Password set successfull")
    else: 
        print("Error occured during validation")
else:
    print("error to short or long enter your ppassword between 8 and 12")