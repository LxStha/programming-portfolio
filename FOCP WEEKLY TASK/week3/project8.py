"""8.Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive."""
num=int(input("enter your require number:"))

if 0<num<12:
    for i in range(13):
        print(f"{i}X{num}={i*num}")

elif num<0:
    for j in range(12, -1, -1):
        print(f"{j}X{num}={j*num}")

else:
    print("invalid number the number should by between 0 and 12")
