"""1.Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original)."""

def to_binary(number):
    
    if number < 0:
        print("Enter a positive number")
    return bin(number)[2:]


num=int(input("Enter a positive integer:"))
print(f"The binary representation of {num} is: {to_binary(num)}")
