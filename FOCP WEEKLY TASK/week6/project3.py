"""3.Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers."""

def check_prime(number):
    fact=0
    for i in range(1, number+1):
        if number%i==0: 
            fact+=1
    
    if fact==2:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

num = int(input("Enter a number: "))
print(check_prime(num))