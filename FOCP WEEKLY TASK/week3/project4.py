"""4.Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']"""

password=input("enter your password:")
confirmed_pass=input("enter your new password:")

Bad_password=['password', 'letmein', 'sesame', 'hello', 'justinbieber']


if 8<=len(password)<=12:
    if password not in Bad_password:
        if password==confirmed_pass:
            print("Password set successfull")
        else: 
            print("Error occured during validation")
    else:
        print("Error")
else:
    print("error to short or long enter your ppassword between 8 and 12 or a bad password")
    
