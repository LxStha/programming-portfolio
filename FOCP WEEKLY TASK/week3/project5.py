"""5.Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time."""

Bad_password=['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password=input("enter your password:")
    confirmed_pass=input("enter your NEW PASSWORD:")

    if 8<=len(password)<=12:   
        if password==confirmed_pass:
            if password not in Bad_password:
                print("Password set successfull")
            else: 
                print("Bad password")
        break
    else:
        print("Error to short or long enter your ppassword between 8 and 12")
        continue