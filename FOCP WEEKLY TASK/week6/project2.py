"""2.Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).
"""
def factors(number):
    factors=[]
    for i in range(1,(number)+1):
        if number%i==0:
            factors.append(i)
    return factors

num=int(input("Enter a number: "))
print("Factors of", num, "are:", factors(num))